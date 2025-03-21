class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def isValid(row, col):
            return 0 <= row < Row and 0 <= col < Col and grid[row][col] == 1 
        
        Row = len(grid)
        Col = len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        queue = deque()
        fresh_count = 0

        for row in range(Row):
            for col in range(Col):
                if grid[row][col] == 1:
                    fresh_count += 1
                elif grid[row][col] == 2:
                    queue.append((row, col, 0))
        
        mins = 0
        while queue:
            row, col, mins = queue.popleft()

            if fresh_count == 0:
                return mins
            
            for dx, dy in directions:
                nextr, nextc = row + dx, col + dy
                if isValid(nextr, nextc):
                    fresh_count -= 1
                    grid[nextr][nextc] = 2
                    queue.append((nextr, nextc, mins+1))
        
        return mins if not fresh_count else -1





