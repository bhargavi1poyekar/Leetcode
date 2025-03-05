class Solution:
    def coloredCells(self, n: int) -> int:
        
        # seen = {(0, 0)}
        # nghbrs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # queue = deque([(0, 0, 1)])

        # while queue:
        #     # print(seen)
        #     row, col, minutes = queue.popleft()

        #     if minutes == n:
        #         # print(seen)
        #         return len(seen)

        #     for dx, dy in nghbrs:
        #         nextr, nextc = row + dx, col + dy
        #         if (nextr, nextc) not in seen:
        #             seen.add((nextr, nextc))
        #             queue.append((nextr, nextc, minutes + 1))

        # return 

        count = 1
        for i in range(1, n):
            count += 4*i
        
        return count

