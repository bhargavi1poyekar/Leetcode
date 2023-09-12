class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        rows=Counter()
        for row in grid:
            rows[tuple(row)]+=1

        columns=Counter()
        for col in range(len(grid[0])):
            column=[]
            for row in range(len(grid)):
                column.append(grid[row][col])
            columns[tuple(column)]+=1
        
        count=0
        for tup in rows:
            count+=rows[tup]*columns[tup]
        
        return count

    
        
        