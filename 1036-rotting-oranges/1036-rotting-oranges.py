class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def valid(row,col):
            return 0<=row<m and 0<=col<n and grid[row][col]==1
        
        directions=[(0,1),(1,0),(0,-1),(-1,0)]

        m=len(grid)
        n=len(grid[0])

        queue=deque()
        fresh_count=0

        for row in range(m):
            for col in range(n):
                if grid[row][col]==2:
                    queue.append((row,col,0))
                if grid[row][col]==1:
                    fresh_count+=1

        steps=0
        while queue:
            row,col,steps=queue.popleft()
            
            for x,y in directions:
                nextr,nextc=row+x,col+y
                if valid(nextr,nextc):
                    fresh_count-=1
                    grid[nextr][nextc]=2
                    queue.append((nextr,nextc,steps+1))
        
        return steps if not fresh_count else -1
        


