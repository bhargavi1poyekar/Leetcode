class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0] # Base case
        
        for row in range(m):
            for col in range(n):
                top = 0
                left = 0
                if row == 0 and col != 0:
                    dp[row][col] = grid[row][col] + dp[row][col-1]
                elif col == 0 and row != 0:
                    dp[row][col] = grid[row][col] + dp[row-1][col]
                elif row != 0 and col != 0:
                    dp[row][col] = grid[row][col] + min(dp[row][col-1], dp[row-1][col])

                # dp[row][col] = grid[row][col] + min(top, left)
        # print(dp)
        return dp[m-1][n-1]
            
        
        # print(dp)
        return dp[m - 1][n - 1]