class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def isValid(row, col):
            return 0 <= row < Row and 0 <= col < Col and maze[row][col] == '.'
        def isExit(row, col):
            return row == 0 or row == Row-1 or col == 0 or col == Col-1

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        Row = len(maze)
        Col = len(maze[0])

        startr, startc = entrance
        queue = deque([(startr, startc, 1)])

        while queue:
            row, col, steps = queue.popleft()
            
            for dx, dy in directions:
                nextr, nextc = row + dx, col + dy
                if isValid(nextr, nextc):
                    if isExit(nextr, nextc):
                        return steps
                    maze[nextr][nextc] = '+'
                    queue.append((nextr, nextc, steps+1))
        
        return -1