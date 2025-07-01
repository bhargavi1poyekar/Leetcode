class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        def house_robber(nums):
            n = len(nums)
            dp = [0]*n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            
            return dp[n-1]
        
        return max(house_robber(nums[:-1]), house_robber(nums[1:]))
        