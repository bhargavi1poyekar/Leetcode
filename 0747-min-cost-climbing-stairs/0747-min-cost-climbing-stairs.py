class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        def dp(i):
            if i <= 1:
                return 0
            
            if i not in memo:
                memo[i] = min(cost[i-1] + dp(i-1), cost[i-2] + dp(i-2))

            return memo[i]

        return dp(len(cost)) 
