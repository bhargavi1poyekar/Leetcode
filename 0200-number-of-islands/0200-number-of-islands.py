class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Understand:

        Given  -> m x n 2d binary grid -> map of 1's land and 0's water

        island -> formed by adjacent lands hori or vertically. 

        Match: Graph Traversal DFS. NUm of connected components. 

        Plan: do normal graph traversal dfs, and for each component increment count. 
        '''

        def isValid(row, col):
            return 0 <= row < Row and 0 <= col < Col and grid[row][col] == '1'

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        Row = len(grid)        
        Col = len(grid[0])


        def dfs(row, col):
            for dx, dy in directions:
                nextr, nextc = row + dx, col + dy
                if isValid(nextr, nextc) and (nextr, nextc) not in seen:
                    seen.add((nextr, nextc))
                    dfs(nextr, nextc)
        
        seen = set()
        num_islands = 0

        for row in range(Row):
            for col in range(Col):
                if isValid(row, col) and (row, col) not in seen:
                    num_islands += 1
                    seen.add((row, col))
                    dfs(row, col)
        
        return num_islands

        '''
        Time Complexity: O(m x n)
        Space COmplexity: O(m*n)
        
        '''
        
