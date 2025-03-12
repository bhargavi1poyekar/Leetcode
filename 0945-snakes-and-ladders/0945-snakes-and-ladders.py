class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        end = n**2
        flat_board = []
        # board_idx = 0

        index = 0
        for i in range(n-1, -1, -1):
            if index % 2 == 0:
                for j in range(n):
                    flat_board.append(board[i][j])
                    # board_idx += 1
            
            else:
                for j in range(n-1, -1, -1):
                    flat_board.append(board[i][j])
                    # board_idx += 1
            index += 1
        
        queue = deque([(0, 0)]) # current square and steps
        seen = {0}

        while queue:
            curr, steps = queue.popleft()

            if flat_board[curr] != -1:
                curr = flat_board[curr] - 1
            
            if curr == end - 1:
                return steps
            
            for next in range((curr + 1), min(curr + 7, end)):
                if next not in seen:
                    seen.add(next)
                    queue.append((next, steps + 1))
        
        return -1 



