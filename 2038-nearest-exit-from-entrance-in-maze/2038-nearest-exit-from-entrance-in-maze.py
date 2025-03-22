class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        def isValid(row, col):
            return 0 <= row < Row and 0 <= col < Col and maze[row][col] == '.'
        
        def isExit(row, col):
            return (row == 0 or row == Row-1 or col == 0 or col == Col-1)
        
        er, ec = entrance
        seen = {(er, ec)}
        queue = deque([(er, ec, 0)])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        Row = len(maze)
        Col = len(maze[0])

        while queue:
            # print(queue)
            row, col, steps = queue.popleft()

            # print(row, col)
            # print(isExit(row, col))
            # print((row != er and col != er))
            if isExit(row, col) and (row, col) != (er, ec):
                return steps
            
            for dx, dy in directions:
                nextr, nextc = row + dx, col + dy
                if isValid(nextr, nextc) and (nextr, nextc) not in seen:
                    seen.add((nextr, nextc))
                    queue.append((nextr, nextc, steps+1))
        
        return -1
