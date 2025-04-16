class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        '''
        Understand:

        Given: 0-indexed n x n int matrix -> grid. 
        Return num pairs r,c -> such that row and column are equal.

        same elements in same order -> equal. 

        Match:
        To check if duplicates -> hash. 

        Plan:
        We need to have row_hash -> with entire row as key, and num of times its is repepated as val. 
        Samae for column. 

        Now, at end, number of Pairs -> num rows * num cols -> that are equal. 

        SO we just traverse over row hash -> and multiply it with count of col for the same val. if no val -> then it will be multiplied by 0, hence that pair won't count. 
        '''

        # Implementation:

        row_hash = Counter()
        for row in grid:
            row_hash[tuple(row)] += 1
        
        col_hash = Counter()
        for col in range(len(grid)):
            column = []
            for row in range(len(grid)):
                column.append(grid[row][col])

            col_hash[tuple(column)] += 1

        num_pairs = 0
        for row in row_hash:
            num_pairs += row_hash[row] * col_hash[row]
        
        return num_pairs
            
        '''
        Time Complexity: O(N*N)
        Space Complexity: O(N*N)
        '''