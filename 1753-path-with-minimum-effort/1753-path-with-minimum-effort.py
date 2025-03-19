class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        def isValid(row, col):
            return 0 <= row < Row and 0 <= col < Col
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def check(effort):
            queue = deque([(0, 0)])
            seen = {(0, 0)}

            while queue:
                row, col = queue.popleft()
                if row == Row-1 and col == Col - 1:
                    return True
                for dx, dy in directions:
                    nextr, nextc = row + dx, col+ dy
                    if isValid(nextr, nextc) and (nextr, nextc) not in seen:
                        if abs(heights[row][col] - heights[nextr][nextc]) <= effort:
                            seen.add((nextr, nextc))
                            queue.append((nextr, nextc))
            return False
        
        Row = len(heights)
        Col = len(heights[0])
        left = 0
        right = max(max(row) for row in heights)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left