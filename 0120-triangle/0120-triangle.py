class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        if not triangle:
            return 0

        Row = len(triangle)

        dp = [[0] * len(triangle[row]) for row in range(Row)]

        dp[0][0] = triangle[0][0]
        # print(dp[0][0])

        for i in range(1, Row):
            len_col = len(triangle[i])
            for j in range(len_col):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == len_col - 1:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        
        # print(dp)
        return min(dp[Row-1])

