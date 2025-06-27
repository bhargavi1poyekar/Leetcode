class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # left_prod = [1]*len(nums)
        # right_prod = [1]*len(nums)

        # # Left product:

        # for i in range(1, len(nums)):
        #     left_prod[i] = left_prod[i-1]*nums[i-1]
        
        # for i in range(len(nums)-2, -1, -1):
        #     right_prod[i] = right_prod[i+1]*nums[i+1]

        # prod = []
        # for i in range(len(nums)):
        #     prod.append(left_prod[i]*right_prod[i])
        
        # return prod

        # 1 array.

        prod = []
        prod.append(1)

        for i in range(len(nums)-1):
            prod.append(prod[i]*nums[i]) 

        # print(prod)
        
        mul = 1
        for i in range(len(nums)-1, -1, -1):
            prod[i] = prod[i]*mul
            mul = nums[i] * mul
        
        return prod






