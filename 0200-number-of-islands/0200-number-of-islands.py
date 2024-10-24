class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        Row = len(grid)
        Col = len(grid[0])

        def isValid(row, col):
            return 0 <= row < Row and 0 <= col < Col and grid[row][col] == "1"
        
        nghbrs = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        num_island = 0

        def dfs(row, col):
            for dx, dy in nghbrs:
                nrow = row + dx
                ncol = col + dy
                if isValid(nrow, ncol) and (nrow, ncol) not in seen:
                    seen.add((nrow, ncol))
                    dfs(nrow, ncol)
                
        seen = set()
        for row in range(Row):
            for col in range(Col):
                if grid[row][col] == '1' and (row, col) not in seen:
                    num_island += 1
                    seen.add((row, col))
                    dfs(row, col)
            
        return num_island


