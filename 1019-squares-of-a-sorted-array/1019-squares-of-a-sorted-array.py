class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        nums_sq = [0]*len(nums)

        left = 0 
        right = len(nums) - 1
        sq_ptr = len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                nums_sq[sq_ptr] = nums[left] ** 2
                left += 1
            else:
                nums_sq[sq_ptr] = nums[right] ** 2
                right -= 1
            sq_ptr -= 1
        
        return nums_sq

