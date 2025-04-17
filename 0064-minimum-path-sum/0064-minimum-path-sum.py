class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        Understand:

        Given -> m x n grid -> non negative num 
        find path from top left to bottom right. 
        minimizes sum 

        return sum

        can move only down or right. 

        Match: Overlapping subproblems + next decision based on current. Minimizing somthing -> Dynamic Programming. 

        Plan:
        
        Function: dp[m][n] -> path with min sum to reach grid[m][n]

        Recurrence Relation -> 
        since it can only move down or rihgt. 

        that means, if we are a cell, then we either came from UP or left.
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        Base Case: dp[0][0] == grid[i][j]
        dp[0][j] => dp[i][j-1] + grid[i][j]
        dp[i][0] => dp[i-1][j] + grid[i][j]
        '''

        # Implement

        m = len(grid)
        n = len(grid[0]) if m else 0

        dp = [[0]*n for _ in range(m)]

        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                
                elif j == 0 and i != 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]

                elif i != 0 and j != 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[m-1][n-1] 

        '''
        Time Complexity: O(m x n)
        Space Complexiyy: O(m x n)
        '''
