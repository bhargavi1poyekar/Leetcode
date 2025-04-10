class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # only go to grids with value 0. 

        def isValid(row, col):
            return 0 <= row < m and 0 <= col < n and obstacleGrid[row][col] == 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0]) if m else 0

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0 

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if isValid(i, j):
                    if isValid(i-1, j):
                        dp[i][j] += dp[i-1][j]
                    if isValid(i, j-1):
                        dp[i][j] += dp[i][j-1]
        
        return dp[m-1][n-1]