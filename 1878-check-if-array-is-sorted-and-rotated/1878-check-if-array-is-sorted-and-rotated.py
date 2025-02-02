class Solution:
    def check(self, nums: List[int]) -> bool:
        
        rotated = False

        for i in range(len(nums)-1):
            diff = nums[i] - nums[i+1]

            if diff > 0:
                if rotated:
                    return False
                rotated = True
        
        if nums[-1] - nums[0] > 0:
            if rotated:
                return False
                
        return True

            
        
        return True
