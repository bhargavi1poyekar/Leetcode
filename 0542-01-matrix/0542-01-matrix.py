class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        def validpath(row,col):
            return 0<=row<rowlen and 0<=col<collen and mat[row][col]==1
        
        rowlen=len(mat)
        collen=len(mat[0])
        queue=deque()
        seen=set()

        for row in range(rowlen):
            for col in range(collen):
                if mat[row][col]==0:
                    seen.add((row,col))
                    queue.append((row,col,1))

        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        while queue:
            row,col,steps=queue.popleft()
            for x,y in directions:
                nextr,nextc=row+x,col+y
                if validpath(nextr,nextc) and (nextr,nextc) not in seen:
                    seen.add((nextr,nextc))
                    queue.append((nextr,nextc,steps+1))
                    mat[nextr][nextc]=steps
        return mat 
