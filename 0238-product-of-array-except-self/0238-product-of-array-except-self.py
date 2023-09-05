class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod=[]
        prod.append(1)

        for i in range(len(nums)-1):
            prod.append(prod[i]*nums[i])

        prev=nums[-1]
        for i in range(len(prod)-2,-1,-1):
            prod[i]=prod[i]*prev
            prev=prev*nums[i]
        
        return prod



        