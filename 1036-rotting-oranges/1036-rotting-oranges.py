class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def isValid(row, col):
            return 0 <= row < Row and 0 <= col < Col and grid[row][col] != 0
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        fresh_count = 0
        seen = set()
        queue = deque()

        Row = len(grid)
        Col = len(grid[0])

        for row in range(Row):
            for col in range(Col):
                if grid[row][col] == 1:
                    fresh_count += 1
                elif grid[row][col] == 2:
                    seen.add((row, col))
                    queue.append((row, col, 0))

        while queue:
            row, col, steps = queue.popleft()
            if grid[row][col] == 1:
                fresh_count -= 1
            
            if not fresh_count:
                return steps
            
            for dx, dy in directions:
                next_r, next_c = row + dx, col + dy
                if isValid(next_r, next_c) and (next_r, next_c) not in seen:
                    seen.add((next_r, next_c))
                    queue.append((next_r, next_c, steps+1))
        
        return -1 if fresh_count != 0 else 0
