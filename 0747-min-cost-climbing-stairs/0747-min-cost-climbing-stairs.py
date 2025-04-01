class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Top Down:

        '''
        def dp(i):
            if i <= 1:
                return 0
            
            if i not in memo:
                memo[i] = min(dp(i-1) + cost[i - 1], dp(i-2) + cost[i - 2]) 
            return memo[i]
        
        memo = {}
        return dp(len(cost))
        '''

        # Bottom Up:
        dp = [0] * (len(cost)+1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[len(cost)]

