class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Understand:

        m x n grid -> can have 1/3 vals
        0 -> empty
        1 -> fresh
        2 -> rotten

        fresh -> 4 directionally adjacent to rotten -> gets rotten -> every min

        min minutes -> no cell has fresh orange. 
        if impossible -> return -1

        Match: Graph (BFS) 
        BFS -> shorted times -> because -> at every minute -> it goes traverses nodes on each level, next min next levels and so on. 

        Plan:

        first keep count of fresh oranges. 
        then add the rotten oranges (row, col) to queue.  -> 0 level
        we can traverse from each rotten orange to its neighbor. 

        we continue BFS till fresh oranges are 0, or queue is empty. 
        '''

        def isValid(row, col):
            # We need to traverse inside boundary of grid, and we are only interested in traversing to fresh orange. 
            return 0 <= row < Row and 0 <= col < Col and grid[row][col] == 1

        Row = len(grid)
        Col = len(grid[0])

        queue = deque()
        seen = set()
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        fresh_count = 0

        for row in range(Row):
            for col in range(Col):
                if grid[row][col] == 1:
                    fresh_count += 1
                elif grid[row][col] == 2:
                    queue.append((row, col, 1))
                    seen.add((row, col))
                
        if not fresh_count:
            return 0

        while queue:
            row, col, min = queue.popleft()

            for dx, dy in directions:
                nextr, nextc = row + dx, col + dy
                if isValid(nextr, nextc) and (nextr, nextc) not in seen:
                    fresh_count -= 1
                    if fresh_count == 0:
                        return min
                    queue.append((nextr, nextc, min + 1))
                    seen.add((nextr, nextc))
        
        return -1

        '''
        Time Complexity: O(M*N)
        Space Complexity: O(M*N)
        '''

               
            
