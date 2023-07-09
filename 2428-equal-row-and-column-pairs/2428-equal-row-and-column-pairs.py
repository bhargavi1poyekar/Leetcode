class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        rows=collections.Counter() # Counter for rows
        cols=collections.Counter() # Counter for columns

        for row in grid:
            rows[tuple(row)]+=1 # add row count
        
        for col in range(len(grid[0])):
            column=[]
            for row in range(len(grid)):
                column.append(grid[row][col]) # Create column
            
            cols[tuple(column)]+=1 # add column count
        
        pair_count=0

        for elem in rows: # for every element in row
            pair_count+=(rows[elem]*cols[elem]) # find the total number of pairs
            # same rows count and same column count will form row*col pairs
            
    
        return pair_count
