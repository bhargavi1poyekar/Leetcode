class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = float('-inf')
        curr = 0

        for num in nums:
            curr = max(curr + num, num)
            max_sum = max(max_sum, curr)
        
        return max_sum