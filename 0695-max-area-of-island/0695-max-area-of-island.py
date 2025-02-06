class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def isValid(row, col):
            return 0 <= row < Row and 0 <= col < Col and grid[row][col]

        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        max_area = 0

        def dfs(row, col):
            if isValid(row, col):
                grid[row][col] = 0
                return 1 + dfs(row, col-1) + dfs(row, col + 1) + dfs(row-1, col) +  dfs(row+1, col)
            return 0

        Row = len(grid)
        Col = len(grid[0])

        for row in range(Row):
            for col in range(Col):
                max_area = max(max_area, dfs(row, col))
        
        return max_area