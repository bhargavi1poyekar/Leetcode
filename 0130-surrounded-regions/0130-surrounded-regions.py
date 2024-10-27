class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def valid(row,col):
            return 0<=row<m and 0<=col<n and board[row][col]=='O'
        
        def dfs(row,col):
            seen.add((row,col))
            for x,y in directions:
                nextr,nextc=row+x,col+y
                if valid(nextr,nextc) and (nextr,nextc) not in seen:
                    dfs(nextr,nextc)

        directions=[(0,1),(1,0),(-1,0),(0,-1)]

        seen=set()

        m=len(board)
        n=len(board[0])

        for row in range(m):
           
            if board[row][0]=='O':
                dfs(row,0)
            
            if board[row][n-1]=='O':
                dfs(row,n-1)
        
        for col in range(n):
            if board[0][col]=='O':
                dfs(0,col)
            if board[m-1][col]=='O':
                # print(board[m-1][col])
                dfs(m-1,col)
        
        for row in range(1,m-1):
            for col in range(1,n-1):
                if board[row][col]=='O' and (row,col) not in seen:
                    board[row][col]='X'
        
        return board
        


