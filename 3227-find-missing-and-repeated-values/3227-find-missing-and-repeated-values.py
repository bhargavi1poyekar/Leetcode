class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        count_list = [0] * (len(grid)**2)
        repeated = 0
        missing = 0

        for i in range(len(grid)):
            for j in range(len(grid)):
                if count_list[grid[i][j] - 1] != 0:
                    repeated = grid[i][j]
                else:
                    count_list[grid[i][j] - 1] =  grid[i][j]
            
        for i in range(len(count_list)):
            if count_list[i] == 0:
                missing = i + 1
        
        return [repeated, missing]

