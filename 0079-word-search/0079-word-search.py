class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def isValid(row, col):
            return 0 <= row < Row and 0 <= col < Col

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        Row = len(board)
        Col = len(board[0])

        def backtrack(row, col, i,  seen):
            if i == len(word):
                return True
            
            for dx, dy in directions:
                nextr, nextc = row + dx, col + dy
                if isValid(nextr, nextc) and (nextr, nextc) not in seen:
                    if board[nextr][nextc] == word[i]:
                        seen.add((nextr, nextc))
                        if backtrack(nextr, nextc, i+1, seen):
                            return True
                        seen.remove((nextr, nextc))
            
            return False
        
        for row in range(Row):
            for col in range(Col):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 1, {(row, col)}):
                        return True
        
        return False