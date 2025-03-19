class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        row_count = Counter()
        col_count = Counter()

        for row in grid:
            row_count[tuple(row)] += 1
        
        for col in range(len(grid)):
            column = []
            for row in range(len(grid)):
                column.append(grid[row][col])

            col_count[tuple(column)] += 1
        
        pairs = 0

        for row in row_count:
            pairs += row_count[row] * col_count[row]

        return pairs
