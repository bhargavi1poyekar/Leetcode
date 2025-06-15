class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(row, col):
            return 0 <= row < Row and 0 <= col < Col and board[row][col] == 'O'
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col):
            if (row, col) not in seen:
                seen.add((row, col))
            
            for dx, dy in directions:
                nextr, nextc = row + dx, col + dy
                if isValid(nextr, nextc) and (nextr, nextc) not in seen:
                    dfs(nextr, nextc)
    
        
        Row = len(board)
        Col = len(board[0])     
        seen = set()

        for row in range(Row):
            if board[row][0] == 'O' and (row, 0) not in seen:
                dfs(row, 0)
            if board[row][Col-1] == 'O' and (row, Col-1) not in seen:
                dfs(row, Col-1)
        
        for col in range(Col):
            if board[0][col] == 'O' and (0, col) not in seen:
                dfs(0, col)
            if board[Row-1][col] == 'O' and (Row-1, col) not in seen:
                dfs(Row-1, col)
        
        for row in range(Row):
            for col in range(Col):
                if (row, col) not in seen and board[row][col] == 'O':
                    board[row][col] = 'X'

        
        


        