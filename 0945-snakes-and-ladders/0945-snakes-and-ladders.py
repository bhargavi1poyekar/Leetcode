class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        end_idx = len(board)**2
        flat_board = []

        i = 0
        for row in range(len(board)-1, -1, -1):
            if i % 2 == 0:
                for col in range(len(board)):
                    flat_board.append(board[row][col])
            else:
                for col in range(len(board)-1, -1, -1):
                    flat_board.append(board[row][col])
            i += 1

        seen = {0}
        queue = deque([(0, 0)])
        # steps = -1

        while queue:
            curr, steps = queue.popleft()

            if flat_board[curr] != -1:
                curr = flat_board[curr] - 1
            elif curr == end_idx - 1:
                return steps

            for next in range(curr+1, min(curr + 7, end_idx)):
                if next not in seen:
                    seen.add(next)
                    queue.append((next, steps+1))
        
        return -1

