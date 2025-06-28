class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sum = 0
        max_sum = float('-inf')
        for num in nums:
            sum = max(num, num + sum)
            max_sum = max(max_sum, sum)
    
        return max_sum