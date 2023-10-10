class Solution:
    def rob(self, nums: List[int]) -> int:

        # def dp(i):
        #     if i==0:
        #         return nums[0]
        #     if i==1:
        #         return max(nums[0],nums[1])
            
        #     if i in memo:
        #         return memo[i]

        #     memo[i]=max(dp(i-1),nums[i]+dp(i-2))
        #     return memo[i]

        # memo={}
        # return dp(len(nums)-1)  
        if len(nums)==1:
            return nums[0]
                  
        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])

        for i in range(2,n):
            dp[i]=max(dp[i-1],nums[i]+dp[i-2])
        
        print(dp)
        return dp[n-1]