class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def valid(row, col):
            return 0 <= row < Row and 0 <= col < Col and grid[row][col] == 1
        
        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        Row = len(grid)
        Col = len(grid[0])

        def dfs(row, col):
            if valid(row, col):
                grid[row][col] = 0
                return 1 + dfs(row, col+1) + dfs(row + 1, col) + dfs(row, col-1) + dfs(row-1, col)
            return 0
        
        max_area = 0
        for i in range(Row):
            for j in range(Col):
                max_area = max(max_area, dfs(i, j))
        
        return max_area