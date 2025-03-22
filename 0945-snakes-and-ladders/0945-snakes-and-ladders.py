class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        level = 0
        flat_board = []
        end = (len(board) ** 2)

        for row in range(len(board)-1, -1, -1):
            if level % 2 == 0:
                for col in range(len(board)):
                    flat_board.append(board[row][col])
            else:
                for col in range(len(board)-1, -1, -1):
                    flat_board.append(board[row][col])
            
            level += 1
        
        queue = deque([(0, 0)]) # square, steps
        seen = {(0)} 

        while queue:
            print(queue)
            square, steps = queue.popleft()

            if flat_board[square] != -1:
                square = flat_board[square]-1

            if square == end - 1:
                return steps
            # print(square)

            for next in range(square + 1, min(square + 7, end)):
                if next not in seen:
                    seen.add(next)
                    queue.append((next, steps + 1))

        return -1  