class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        Row = len(matrix)
        Col = len(matrix[0]) if Row else 0
        dp = [[0] * (Col+1) for _ in range(Row+1)]
        max_side = 0

        for i in range(1, Row+1):
            for j in range(1, Col+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                    max_side = max(max_side, dp[i][j])
        
        return max_side * max_side