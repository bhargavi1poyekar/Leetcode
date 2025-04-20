class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        Understand:

        Given: an int arr -> cost
        cost[i] -> cost of ith step 

        once paid -> either climb one or 2 steps. 

        can start from 0 or 1. 

        Return min cost to reach top of floor.

        Match: Dynamic Programming. 

        Plan:

        dp[i] -> min cost to reach ith floor. 

        recurrence relation -> if you are at i, you either reached from i-2 or i-1. 
        so dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])

        Base Case: if i <= 1: dp = 0
        '''

        def dp(i):
            if i <= 1:
                return 0
            
            if i not in memo:
                memo[i] = min(cost[i-1] + dp(i-1), cost[i-2] + dp(i-2))
            
            return memo[i]
        
        memo = {}
        return dp(len(cost))

        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''