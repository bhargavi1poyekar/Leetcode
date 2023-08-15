class Solution:
    def climbStairs(self, n: int) -> int:

        def dp(i):

            if i<=2:
                return i
            
            if i in memo:
                return memo[i]
            
            memo[i]=dp(i-1)+dp(i-2)
            return memo[i]
        
        memo={}
        return dp(n)