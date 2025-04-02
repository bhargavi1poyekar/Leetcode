class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def isValid(row, col):
            return row >= 0 and col >= 0 and obstacleGrid[row][col] == 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 # Base case
        
        for row in range(m):
            for col in range(n):
                if isValid(row, col):
                    if isValid(row-1, col):
                        dp[row][col] += dp[row - 1][col]
                    if isValid(row, col-1):
                        dp[row][col] += dp[row][col - 1]
                else:
                    dp[row][col] == 0
        
        # print(dp)
        return dp[m - 1][n - 1]