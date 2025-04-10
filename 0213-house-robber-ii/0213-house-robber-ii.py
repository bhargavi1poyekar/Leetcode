class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def regular_house_robber(nums):
            # def dp(i):
            #     if i == 0:
            #         return nums[0]
            #     if i == 1:
            #         return max(nums[0], nums[1])
                
            #     if i not in memo:
            #         memo[i] = max(dp(i-1), dp(i-2) + nums[i])
                
            #     return memo[i]

            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])

            return dp[len(nums)-1]
        
        return max(regular_house_robber(nums[1:]), regular_house_robber(nums[:-1]))