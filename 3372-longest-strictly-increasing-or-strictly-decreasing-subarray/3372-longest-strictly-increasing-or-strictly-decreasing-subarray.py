class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        max_length = 1

        # CHeck for strictly inc first. 

        left = 0
        for right in range(1, len(nums)):
            if nums[right] <= nums[right-1]:
                left = right

            max_length = max(max_length, right - left + 1)

        left = 0
        for right in range(1, len(nums)):
            if nums[right] >= nums[right-1]:
                left = right

            max_length = max(max_length, right - left + 1)
        
        return max_length

