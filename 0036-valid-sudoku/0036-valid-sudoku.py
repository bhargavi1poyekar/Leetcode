class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n=9
        rows=[set() for i in range(n)]
        cols=[set() for i in range(n)]
        boxes=[set() for i in range(n)]

        for r in range(9):
            for c in range(9):
                val=board[r][c]

                if val=='.':
                    continue
                
                if val in rows[r]:
                    return False
                
                rows[r].add(val)

                if val in cols[c]:
                    return False
                
                cols[c].add(val)

                box_idx=(r//3)*3+(c//3)
                
                if val in boxes[box_idx]:
                    return False
                
                boxes[box_idx].add(val)
        
        return True





