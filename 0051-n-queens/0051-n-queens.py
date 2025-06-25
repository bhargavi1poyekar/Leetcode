class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # Create duplicate of state
        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board

        def backtrack(row, cols, left_diags, right_diags, state):
            if row == n:
                ans.append(create_board(state))
                return 
            
            count = 0
            for col in range(n):
                left_diag = row - col
                right_diag = row + col

                if col in cols or left_diag in left_diags or right_diag in right_diags:
                    continue
                
                cols.add(col)
                left_diags.add(left_diag)
                right_diags.add(right_diag)
                state[row][col]="Q"

                backtrack(row+1, cols, left_diags, right_diags, state)

                cols.remove(col)
                left_diags.remove(left_diag)
                right_diags.remove(right_diag)
                state[row][col]="."
        
        ans = []
        empty_board=[["."]*n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return ans