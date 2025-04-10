class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        Row = len(grid)
        Col = len(grid[0]) if Row else 0

        dp = [[0] * Col for _ in range(Row)]

        dp[0][0] = grid[0][0]

        for i in range(Row):
            for j in range(Col):
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                elif i > 0 and j > 0:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        
        return dp[Row-1][Col-1]