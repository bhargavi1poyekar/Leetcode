class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def isValid(row, col):
            return 0 <= row < Row and 0 <= col < Col
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        Row = len(heights)
        Col = len(heights[0])
        
        def dfs(row, col, seen):
            seen.add((row, col))

            for dx, dy in directions:
                nextr, nextc = row + dx, col + dy
                if isValid(nextr, nextc) and (nextr, nextc) not in seen and heights[nextr][nextc] >= heights[row][col]:
                    dfs(nextr, nextc, seen)
        
            
        
        Pacific = set()
        Atlantic = set()

        for i in range(Row):
            dfs(i, 0, Pacific)
            dfs(i, Col-1, Atlantic)
        
        for i in range(Col):
            dfs(0, i, Pacific)
            dfs(Row-1, i, Atlantic)
    
        return list(Pacific.intersection(Atlantic))
