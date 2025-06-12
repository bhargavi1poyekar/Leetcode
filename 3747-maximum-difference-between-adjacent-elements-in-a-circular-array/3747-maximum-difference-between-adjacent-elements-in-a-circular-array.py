class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        
        diff = 0
        max_diff = abs(nums[0]-nums[-1])

        for i in range(1, len(nums)):
            diff = abs(nums[i] - nums[i-1])
            max_diff = max(diff, max_diff)
        
        return max_diff
