class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0]:
            return -1
        
        def isValid(row, col):
            return 0 <= row < Row and 0 <= col < Col and (not grid [row][col])
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        seen = {(0, 0)}
        queue = deque([(0, 0, 1)])

        Row = len(grid)
        Col = len(grid[0])

        while queue:
            row, col, steps = queue.popleft()

            if row == Row - 1 and col == Col - 1:
                return steps
            
            for dx, dy in directions:
                nextr, nextc = row + dx, col + dy
                if isValid(nextr, nextc) and (nextr, nextc) not in seen:
                    seen.add((nextr, nextc))
                    queue.append((nextr, nextc, steps+1))
        
        return -1
