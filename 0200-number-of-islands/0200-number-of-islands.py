class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def isValid(row, col): 
            return 0 <= row < Row and 0 <= col < Col and grid[row][col] == '1'
        nghbrs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col):
            for dx, dy in nghbrs:
                newr = row + dx
                newc = col + dy

                if isValid(newr, newc) and (newr, newc) not in seen:
                    seen.add((newr, newc))
                    dfs(newr, newc)
        
        Row = len(grid)
        Col = len(grid[0])

        seen = set()
        num_islands = 0

        for row in range(Row):
            for col in range(Col):
                if isValid(row, col) and (row, col) not in seen:
                    seen.add((row, col))
                    num_islands += 1
                    dfs(row, col)
        
        return num_islands
