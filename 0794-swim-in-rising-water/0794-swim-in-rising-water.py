class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)

        directions=[(0,1),(1,0),(0,-1),(-1,0)]

        def is_valid(row,col):
            return 0<=row<N and 0<=col<N

        def check(time_limit):
            queue=deque([(0, 0)])
            visited = {(0, 0)}

            while queue:
                row, col = queue.popleft()
                if row == col == N - 1:
                    return True
                    
                for dx,dy in directions:
                    nrow,ncol=row+dx,col+dy
                    if is_valid(nrow,ncol) and (nrow, ncol) not in visited and grid[nrow][ncol] <= time_limit:
                        queue.append((nrow, ncol))
                        visited.add((nrow, ncol))

            return False
        
        left, right = grid[0][0], N * N

        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right=mid
            else:
                left=mid+1

        return left
