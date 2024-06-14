class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        # moves = 0
        # unique_hash = {}
        
        # for i in range(len(nums)):
            
        #     while nums[i] in unique_hash:
        #         nums[i] += 1 

        nums.sort()
        numTracker = 0
        minIncreament = 0

        for num in nums:
            numTracker = max(numTracker, num)
            minIncreament += numTracker - num
            numTracker += 1
        return minIncreament