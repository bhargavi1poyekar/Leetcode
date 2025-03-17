class Solution:
    def totalNQueens(self, n: int) -> int:

        def backtrack(row, diags, antidiags, cols):
            if row == n:
                return 1 # return 1 solution

            solutions = 0

            for col in range(n):
                curr_diag = row - col
                curr_anti_diag = row + col

                if col in cols or curr_diag in diags or curr_anti_diag in antidiags:
                    continue
                
                cols.add(col)
                diags.add(curr_diag)
                antidiags.add(curr_anti_diag)

                solutions += backtrack(row+1, diags, antidiags, cols)

                cols.remove(col)
                diags.remove(curr_diag)
                antidiags.remove(curr_anti_diag)
            
            return solutions

        return backtrack(0, set(), set(), set())

        