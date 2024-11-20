class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        def square(num):
            return num ** 2
        
        left = 0
        right = len(nums) - 1

        square_arr = [0] * len(nums)
        ptr = len(nums) - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                square_arr[ptr] = square(nums[left])
                left += 1
            else:
                square_arr[ptr] = square(nums[right])
                right -= 1
            
            ptr -= 1
        
        return square_arr
