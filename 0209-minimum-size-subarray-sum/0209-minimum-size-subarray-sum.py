class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        min_length = len(nums)+1
        curr_sum = 0
        
        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                min_length = min(min_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            
        return min_length if min_length != (len(nums)+1) else 0 