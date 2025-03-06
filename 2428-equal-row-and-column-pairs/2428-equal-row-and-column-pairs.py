class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        rows = Counter()
        cols = Counter()

        for row in grid:
            rows[(tuple(row))] += 1
        
        for col in range(len(grid[0])):
            column = []
            for row in range(len(grid)):
                column.append(grid[row][col])

            cols[tuple(column)] += 1
        
        pair_count = 0
        for elem in rows:
            pair_count += rows[elem] * cols[elem]
        
        return pair_count
