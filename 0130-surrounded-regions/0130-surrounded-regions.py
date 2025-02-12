class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(row, col):
            return 0 <= row < Row and 0 <= col < Col and board[row][col] == 'O'

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col):
            seen.add((row, col))
            for dx, dy in directions:
                next_r, next_c = row + dx, col + dy
                if isValid(next_r, next_c) and (next_r, next_c) not in seen: 
                    dfs(next_r, next_c)
            
        Row = len(board)
        Col = len(board[0])
        seen = set()

        for row in range(Row):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][Col-1] == 'O':
                dfs(row, Col-1)
        
        for col in range(Col):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[Row-1][col] == 'O':
                dfs(Row-1, col)

        for row in range(Row):
            for col in range(Col):
                if board[row][col] == 'O' and (row, col) not in seen:
                    board[row][col] = 'X'
        
        return board
