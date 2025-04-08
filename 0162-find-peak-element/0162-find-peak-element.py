class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
            
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        
        return left