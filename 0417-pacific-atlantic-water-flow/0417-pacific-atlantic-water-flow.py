class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def isValid(row, col):
            return 0 <= row < Row and 0 <= col < Col
        
        Row = len(heights)
        Col =  len(heights[0])

        atlantic = set()
        pacific = set()

        directions = [(0,1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col, ocean):
            ocean.add((row, col))
            for dx, dy in directions:
                nextr, nextc = row + dx, col + dy
                if isValid(nextr, nextc) and heights[nextr][nextc] >= heights[row][col] and (nextr, nextc) not in ocean:
                    dfs(nextr, nextc, ocean)
        
        for row in range(Row):
            dfs(row, 0, pacific)
            dfs(row, Col-1, atlantic)
        
        for col in range(Col):
            dfs(0, col, pacific)
            dfs(Row-1, col, atlantic)
        
        return list(pacific.intersection(atlantic))


