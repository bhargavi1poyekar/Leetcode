class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def isValid(row, col):
            return 0 <= row < Row_len and 0 <= col < Col_len
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col, seen):
            for dx, dy in directions:
                next_r, next_c = row + dx, col + dy
                if (next_r, next_c) not in seen and isValid(next_r, next_c):
                    if heights[next_r][next_c] >= heights[row][col]:
                        seen.add((next_r, next_c))
                        dfs(next_r, next_c, seen)
        
        Row_len = len(heights)
        Col_len = len(heights[0])
        Pacific_seen = set()
        Atlantic_seen = set()

        for row in range(Row_len):
            Pacific_seen.add((row, 0))
            dfs(row, 0, Pacific_seen)
            Atlantic_seen.add((row, Col_len-1))
            dfs(row, Col_len-1, Atlantic_seen)
        
        for col in range(Col_len):
            Pacific_seen.add((0, col))
            dfs(0, col, Pacific_seen)
            Atlantic_seen.add((Row_len-1, col))
            dfs(Row_len-1, col, Atlantic_seen)
        
        return list(Pacific_seen.intersection(Atlantic_seen))