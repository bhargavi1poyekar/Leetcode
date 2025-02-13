class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        def isValid(row, col):
            return 0 <= row < Row and 0 <= col < Col 
        
        Row = len(grid)
        Col = len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        seen = {(0, 0, k)} # row, col, k
        queue = deque([(0, 0, k, 0)]) # row, col, k, steps

        while queue:
            row, col, obst_remain, steps = queue.popleft()

            if row == Row-1 and col == Col-1:
                return steps

            for dx, dy in directions:
                next_r = row + dx
                next_c = col + dy
                if isValid(next_r, next_c) and (next_r, next_c, obst_remain) not in seen:
                    if grid[next_r][next_c] == 0:
                        seen.add((next_r, next_c, obst_remain))
                        queue.append((next_r, next_c, obst_remain, steps+1))

                    elif grid[next_r][next_c] and obst_remain:
                        seen.add((next_r, next_c, obst_remain))
                        queue.append((next_r, next_c, obst_remain-1, steps+1))
        
        return -1




