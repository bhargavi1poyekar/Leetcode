class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        squares = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        ptr = len(nums) - 1

        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                squares[ptr] = nums[left] ** 2
                left += 1
            else:
                squares[ptr] = nums[right] ** 2
                right -= 1
            
            ptr -= 1
        
        return squares



        