class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        def isValid(r,c):
            return 0 <= r < row and 0 <= c < col 
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def check(day):
            visited=[[0 for i in range(col)] for i in range(row)]

            queue=deque()

            for i, j in cells[:day]:
                visited[i-1][j-1]=1
            
            for c in range(col):
                if not visited[0][c]:
                    queue.append((0,c))
                    visited[0][c]=1
                
            while queue:
                r,c = queue.popleft()

                if r == row - 1:
                    return True

                for dx,dy in directions:
                    x,y = r + dy, c + dx

                    if isValid(x,y) and visited[x][y] == 0:
                        queue.append((x,y))
                        visited[x][y] = 1
            return False
    
    
        left, right = 1, row * col

        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return right

