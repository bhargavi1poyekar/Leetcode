class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i] == 0:
                continue
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        result = [0] * len(nums)
        idx = 0
        for num in nums:
            if num != 0:
                result[idx] = num
                idx += 1
        
        return result
            

            
