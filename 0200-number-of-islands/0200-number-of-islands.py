class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def isValid(row, col):
            return 0 <= row < Row and 0 <= col < Col and grid[row][col] == '1'
        
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def dfs(row, col):
            for dx, dy in directions:
                nextr, nextc = row + dx, col + dy
                if isValid(nextr, nextc) and (nextr, nextc) not in seen:
                    seen.add((nextr, nextc))
                    dfs(nextr, nextc)
        
        Row = len(grid)
        Col = len(grid[0])
        seen = set()

        num_islands = 0

        for row in range(Row):
            for col in range(Col):
                if isValid(row, col) and (row, col) not in seen:
                    num_islands += 1
                    seen.add((row, col))
                    dfs(row, col)
        
        return num_islands
        


