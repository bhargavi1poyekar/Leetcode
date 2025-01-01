class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] % 2 == 1 and nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            elif nums[left] % 2 == 1:
                right -= 1
            else:
                left += 1
        
        return nums
    