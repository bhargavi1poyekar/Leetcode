class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        if not triangle:
            return 0

        dp = [[0] * len(triangle[row]) for row in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        Row = len(triangle)

        for row in range(1, len(triangle)):
            Col = len(triangle[row])
            for col in range(len(triangle[row])):
                if col == 0:
                    dp[row][col] = dp[row-1][col] + triangle[row][col]
                elif col == Col - 1:
                    dp[row][col] = dp[row-1][col-1] + triangle[row][col]
                else:
                    dp[row][col] = min(dp[row-1][col], dp[row-1][col-1]) + triangle[row][col]
        
        return min(dp[Row-1])
                    
