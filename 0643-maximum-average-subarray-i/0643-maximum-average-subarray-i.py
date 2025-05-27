class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        max_sum = float('-inf')
        curr_sum = 0
        left = 0

        for right in range(k):
            curr_sum += nums[right]
        
        max_sum = curr_sum

        for right in range(k, len(nums)):
            curr_sum += nums[right] - nums[left] 
            max_sum = max(max_sum, curr_sum)
            left += 1
        
        return max_sum/k
