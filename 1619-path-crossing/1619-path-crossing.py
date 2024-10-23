class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited=set()
        x=0
        y=0
        visited.add((0,0))
        coord = {'N':(0,1), 'S':(0,-1), 'E':(1, 0), 'W':(-1, 0)}
        for i in range(len(path)):
            dx, dy = coord[path[i]]
            x += dx
            y += dy
            if (x,y) in visited:
                return True
            else:
                visited.add((x,y))
        
        return False