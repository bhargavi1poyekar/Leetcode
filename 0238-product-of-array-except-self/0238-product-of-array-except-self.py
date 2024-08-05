class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_prod = [1]
        right_prod = [1] * len(nums)

        for i in range(len(nums) - 1):
            curr_prod = left_prod[i] * nums[i]
            left_prod.append(curr_prod)

        for i in range(len(nums)-1, 0, -1):
            curr_prod = right_prod[i] * nums[i]
            right_prod[i-1] = curr_prod
        

        for i in range(len(nums)):
            left_prod[i] = left_prod[i] * right_prod[i]
        
        return left_prod