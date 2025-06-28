class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        m = len(matrix)
        n = len(matrix[0])
        right = m * n - 1

        while left <= right:
            mid = left + (right-left) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False