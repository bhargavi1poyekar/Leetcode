class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        Understand:

        Given -> m x n binary matrix  -> 0 or 1 vals. 
        find largest square -> with only 1's -> return the area. 

        Match: if a square has 1 -> it alone also is a square. And it participates in building other squares -> so we can use Dynamic programming. 

        Plan:
        dp[m][n] => find the length of square this help into forming. 

        state vars -> 2 -> rows and cols. 

        Base Case -> for first square -> initially length is 0. 

        Recurrence Relation -> get min(dp[m-1][j-1], dp[m][n-1], dp[m-1][n]) + 1 (if curr square is 1)

        this is the side. we keep updating the max side. 

        at end we return max side square. 
        '''

        Row = len(matrix)
        Col = len(matrix[0]) if Row else 0
        dp = [[0] * (Col+1) for _ in range(Row+1)]

        max_side = 0

        for i in range(1, Row+1):
            for j in range(1, Col+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                    max_side = max(max_side, dp[i][j])
                
        return max_side ** 2
