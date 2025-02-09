class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        def valid(row,col):
            return 0<=row<m and 0<=col<n and grid[row][col]==1

        def dfs(row,col):
            for x,y in directions:
                nextr,nextc=row+x,col+y
                if valid(nextr,nextc):
                    grid[nextr][nextc]=0
                    dfs(nextr,nextc)

        def border(row,col):
            return row==0 or row==m-1 or col==0 or col==n-1
        
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        m=len(grid)
        n=len(grid[0])
        
        no_boundary=0

        for row in range(m):
            for col in range(n):
                if border(row,col) and grid[row][col]:
                    grid[row][col]=0
                    dfs(row,col)
        
        for row in range(m):
            for col in range(n):
                if grid[row][col]:no_boundary+=1
        
        return no_boundary
                   
            

        

                


