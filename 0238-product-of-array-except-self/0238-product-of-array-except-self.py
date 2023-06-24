class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod=1
        ans=[1 for i in range(len(nums))]

        for i in range(len(nums)):
            ans[i]=prod
            prod*=nums[i]
        
        prod=1
        for i in range(len(nums)-2,-1,-1):
            ans[i]=prod*nums[i+1]*ans[i]
            prod*=nums[i+1]
        return ans


        
