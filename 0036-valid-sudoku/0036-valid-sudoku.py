class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows_hash=[set() for i in range(9)]
        cols_hash=[set() for i in range(9)]
        boxes_hash=[set() for i in range(9)]

        for row in range(len(board)):
            for col in range(len(board[0])):
                val=board[row][col]
                if val=='.':
                    continue

                if val in rows_hash[row]:
                    return False
                
                rows_hash[row].add(val)
                
                if val in cols_hash[col]:
                    return False
                
                cols_hash[col].add(val)
                
                box_idx=(row//3)*3+(col//3)
                if val in boxes_hash[box_idx]:
                    return False
                
                boxes_hash[box_idx].add(val)
        
        return True


        