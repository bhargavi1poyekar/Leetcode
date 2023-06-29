class Solution:
    def isPathCrossing(self, path: str) -> bool:

        x=0
        y=0
        coord={}
        coord[(0,0)]=1

        for i in path:
            if i=='N':
                y+=1
            elif i=='S':
                y-=1
            elif i=='E':
                x+=1
            else:
                x-=1
            # print(x,y,coord)
            if (x,y) in coord:
                return True
            else: coord[(x,y)]=1
        
        return False