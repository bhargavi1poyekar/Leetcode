class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = float('-inf')
        curr = float('-inf')
        
        for num in nums:
            curr = max(num, curr + num)
            max_sum = max(max_sum, curr)
        
        return max_sum