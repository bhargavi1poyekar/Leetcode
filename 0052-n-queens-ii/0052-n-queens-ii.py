class Solution:
    def totalNQueens(self, n: int) -> int:
    
        def backtrack(row, cols, left_diags, right_diags):
            if row == n:
                return 1
            
            count = 0
            for col in range(n):
                left_diag = row - col
                right_diag = row + col

                if col in cols or left_diag in left_diags or right_diag in right_diags:
                    continue
                
                cols.add(col)
                left_diags.add(left_diag)
                right_diags.add(right_diag)

                count += backtrack(row+1, cols, left_diags, right_diags)

                cols.remove(col)
                left_diags.remove(left_diag)
                right_diags.remove(right_diag)

            return count
        
        return backtrack(0, set(), set(), set())


