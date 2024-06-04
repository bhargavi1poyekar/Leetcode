class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n<3:
            return n
        dp = [0] * (n)
        dp[0] = 1
        dp[1] = 2
        dp[2] = 5
        for i in range(3,len(dp)):
            dp[i] = (dp[i-1]*2 + dp[i-3]) % MOD
        return dp[n-1]