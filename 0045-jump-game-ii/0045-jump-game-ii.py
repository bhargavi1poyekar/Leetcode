class Solution:
    def jump(self, nums: List[int]) -> int:
        
        left = 0
        right = 0
        num_jump = 0

        while right < len(nums) - 1:
            max_jump = 0

            for i in range(left, right+1):
                max_jump = max(max_jump, i + nums[i])
            
            left = right + 1
            right = max_jump

            num_jump += 1
        
        return num_jump
