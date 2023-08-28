class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod=[1]*len(nums)

        for i in range(1,len(nums)):
            prod[i]=nums[i-1]*prod[i-1]
        
        last=1
        for i in range(len(nums)-2,-1,-1):
            # print(last,prod[i],nums[i+1])
            prod[i]=last*prod[i]*nums[i+1]
            last*=nums[i+1]
        
        return prod




        