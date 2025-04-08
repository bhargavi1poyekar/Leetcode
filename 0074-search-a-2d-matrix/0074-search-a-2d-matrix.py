class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        '''
        Understand -> searching in 2d matrix. 

        each row -> non decreasing order. 
        start element of row > last element of prev row. 

        Match:
        1. Normal Linear Search -> O(m*n)
        2. Binary Search. -> O(log(m*n))

        Plan:

        implement normal binary search. By reducing search space to half at every iteration. 
        But from mid -> how to get the cell. 

        n = len(columns)

        row = mid // n
        col = mid % n

        m = 3, n = 4
        
           0  1  2  3
        0  1  3  5  7
        1  10 11 16 20
        2  23 30 34 60

        mid = left + right // 2 -> 0 + 12 // 2  -> 6 -> should be 12 (starting with 0 index)
        row = mid // n -> 6 // 4 -> 1 -> 1th row.
        col = mid % n -> 6 % 4 -> 2 -> 2nd col  
        nums[row][col] => 12
        '''
        
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = (m*n) - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
        
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False

        '''
        Time Complexity -> O(log(m*n))
        Space Complexity -> O(1)
        '''