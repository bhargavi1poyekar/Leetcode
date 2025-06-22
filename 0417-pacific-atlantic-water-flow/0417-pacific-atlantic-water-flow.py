class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def isValid(row, col):
            return  0 <= row < Row and 0 <= col < Col
        
        Row = len(heights)
        Col = len(heights[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        pacific_set = set()
        atlantic_set = set()

        def dfs(row, col, seen):
            if (row, col) not in seen:
                seen.add((row, col))
            else:
                return
            
            for dx, dy in directions:
                nextr, nextc = row + dx, col + dy
                if isValid(nextr, nextc) and heights[nextr][nextc] >= heights[row][col]:
                    dfs(nextr, nextc, seen)

        for row in range(Row):
            dfs(row, 0, pacific_set) # Left border
            dfs(row, Col-1, atlantic_set) # Right border
        
        for col in range(Col):
            dfs(0, col, pacific_set) # Top border
            dfs(Row-1, col, atlantic_set) # Bottom border
        
        return list(pacific_set.intersection(atlantic_set))
        
