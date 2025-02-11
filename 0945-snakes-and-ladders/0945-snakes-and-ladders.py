class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        end = n*n

        flat_board = []

        index = 0 # If even -> straight append, if odd -> reverse append

        for row in range(n-1, -1, -1):
            if index % 2 == 0:
                for col in range(n):
                    flat_board.append(board[row][col])
            else:
                for col in range(n-1, -1, -1):
                    flat_board.append(board[row][col])
            
            index += 1

        queue = deque([(0, 0)])
        seen = {0}

        while queue:
            node, steps = queue.popleft()

            if flat_board[node] != -1:
                node = flat_board[node]-1
            
            if node == end-1:
                return steps
            
            for next in range(node+1, min(node+7, end)):
                if next not in seen:
                    seen.add(next)
                    queue.append((next, steps+1))

        return -1 



