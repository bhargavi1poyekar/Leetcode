class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        num_islands = 0

        Row = len(grid)
        Col = len(grid[0])
        seen = set()

        def isvalid(row, col):
            return 0 <= row < Row and 0 <= col < Col and grid[row][col] == '1'

        nghbrs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            for dx, dy in nghbrs:
                next_r, next_c = row + dx, col + dy
                if isvalid(next_r, next_c) and (next_r, next_c) not in seen:
                    seen.add((next_r, next_c))
                    dfs(next_r, next_c)

        for row in range(Row):
            for col in range(Col):
                if isvalid(row, col) and (row, col) not in seen:
                    num_islands += 1
                    seen.add((row, col))
                    dfs(row, col)
            
        return num_islands

