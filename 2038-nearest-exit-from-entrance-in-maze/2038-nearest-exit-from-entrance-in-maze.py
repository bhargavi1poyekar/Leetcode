class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(row,col):
            return 0<=row<m and 0<=col<n and maze[row][col]=='.'

        e_row,e_col=entrance
        queue=deque([(e_row,e_col,1)])
        seen={(e_row,e_col)}

        directions=[(0,1),(1,0),(-1,0),(0,-1)]

        m=len(maze)
        n=len(maze[0])

        while queue:
            row,col,steps=queue.popleft()

            for x,y in directions:
                nextr,nextc=row+x,col+y
                

                if valid(nextr,nextc) and (nextr,nextc) not in seen:
                    if (nextr==0 or nextr==m-1 or nextc==0 or nextc==n-1):
                        return steps
                    seen.add((nextr,nextc))
                    queue.append((nextr,nextc,steps+1))
        
        return -1