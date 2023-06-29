class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        rows=collections.Counter()
        for row in grid:
            rows[tuple(row)]+=1
        
        cols=collections.Counter()
        for col in range(len(grid[0])):
            column=[]
            for row in range(len(grid)):
                column.append(grid[row][col])
            
            cols[tuple(column)]+=1
        
        count=0
        for elem in rows:
            count+=rows[elem]*cols[elem]
        
        return(count)


