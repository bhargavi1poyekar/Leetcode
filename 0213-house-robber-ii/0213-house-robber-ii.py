class Solution:
    def rob(self, nums: List[int]) -> int:
        
        '''
        Understand:

        rob houses. each house has certain money. Nums[i]

        arranged in circle. first is neighbor or last one. 

        adjacent houses have security -> and no two adjacent houses can be robbed. 

        return max amt of money you can rob. 

        Match: Dynamic Programming -> overlapping subproblem. and next decision based on current decision. 

        Plan:
        have a function for normal house robber. 
        Here the only diff is circular arr. 
        So if 1st house is robbed, we cannot take last house. 
        and if last is robbed, we cannot take first. 

        So we do house robber on nums[:-1] and nums[1:] and take max from these amounts.   
        '''

        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def house_robber(nums):
            dp = [0] * len(nums)

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
            return dp[len(nums)-1]

        return max(house_robber(nums[:-1]), house_robber(nums[1:]))

        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
