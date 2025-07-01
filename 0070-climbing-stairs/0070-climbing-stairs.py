class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dp(n):
            if n <= 2:
                return n
            
            if n not in memo:
                memo[n] = dp(n-1) + dp(n-2)
            
            return memo[n]
        
        memo = {}
        return dp(n)