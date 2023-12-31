class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        m=len(grid)
        n=len(grid[0])

        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        ans=[]

        s_row,s_col=0,0
        empty=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]>=0:
                   empty+=1
                if grid[i][j]==1:
                    s_row,s_col=i,j
        
        
        path_count=0

        def backtrack(row, col, remain):
            
            nonlocal path_count

            # base case
            # print(row,col, remain)
            if grid[row][col] == 2 and remain == 0:
                path_count += 1
                print('reached')
                return
            
            for x,y in directions:
                next_r, next_c= row+x,col+y
                if valid(next_r,next_c) and grid[next_r][next_c]>=0:
                    temp = grid[row][col] 
                    grid[row][col] = -4
                    backtrack(next_r, next_c, remain-1)
                    grid[row][col] = temp

        backtrack(s_row, s_col, empty-1)

        return path_count
                
                    



