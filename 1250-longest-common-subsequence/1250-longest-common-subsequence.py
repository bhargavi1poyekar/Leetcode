class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        T1 = len(text1)
        T2 = len(text2)

        dp = [[0] * (T2+1) for _ in range(T1+1)]

        for i in range(T1-1, -1, -1):
            for j in range(T2-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        
        return dp[0][0]

        