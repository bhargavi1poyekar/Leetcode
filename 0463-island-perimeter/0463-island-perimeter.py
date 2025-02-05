class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def isValid(row, col):
            return 0 <= row < Row and 0 <= col < Col and grid[row][col]
            
        def dfs(row, col):
            if not isValid(row, col):
                return 1
            if (row, col) in seen:
                return 0
            seen.add((row, col))
            return dfs(row, col+1) + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col-1)
        
        seen = set()
        Row = len(grid)
        Col = len(grid[0])

        for row in range(Row):
            for col in range(Col):
                if grid[row][col] == 1:
                    return dfs(row, col)
            
        