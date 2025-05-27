class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        count_zero = 0
        left = 0

        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count_zero += 1

            while count_zero > 1:
                if nums[left] == 0:
                    count_zero -= 1
                left += 1
            
            max_length = max(max_length, right - left)
        
        return max_length
