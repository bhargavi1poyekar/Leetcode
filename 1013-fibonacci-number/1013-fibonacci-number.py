class Solution:
    def fib(self, n: int) -> int:

        # Bottom Up:

        if n<2:
            return n 

        dp=[0,1]
        for i in range(2,n+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n]


        ## Top-down

#         if n<2:
#             return n
        
#         if n in memo:
#             return memo[n]
        
#         memo[n]=self.fib(n-1)+self.fib(n-2)
#         return memo[n]
        
# memo={}