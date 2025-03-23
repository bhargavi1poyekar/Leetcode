class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def isValid(row, col):
            return 0 <= row < Row and 0 <= col < Col and grid[row][col] == 1
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        Row = len(grid)
        Col = len(grid[0])
        
        queue = deque()
        seen = set()
        fresh_count = 0

        for row in range(Row):
            for col in range(Col): 
                if grid[row][col] == 1:
                    fresh_count += 1
                elif grid[row][col] == 2:
                    queue.append((row, col, 1))
                    seen.add((row, col))

        if not fresh_count:
            return 0
            
        while queue:
            row, col, mins = queue.popleft()

            for dx, dy in directions:
                nextr, nextc = row + dx, col + dy
                if isValid(nextr, nextc) and (nextr, nextc) not in seen:
                    fresh_count -= 1
                    if fresh_count == 0:
                        return mins
                    seen.add((nextr, nextc))
                    queue.append((nextr, nextc, mins + 1))
        
        return -1