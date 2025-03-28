class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        left = 0
        max_length = 0
        non_one = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                non_one += 1
            
            while non_one > 1:
                if nums[left] == 0:
                    non_one -= 1
                
                left += 1
            
            max_length = max(max_length, right - left)
        
        return max_length
            

