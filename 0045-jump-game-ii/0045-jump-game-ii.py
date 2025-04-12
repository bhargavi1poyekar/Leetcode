class Solution:
    def jump(self, nums: List[int]) -> int:
        
        l_ptr = 0
        r_ptr = 0

        max_jump = 0 
        num_jmps = 0

        while r_ptr < len(nums) - 1:
            for i in range(l_ptr, r_ptr + 1):
                max_jump = max(max_jump, i + nums[i])
            
            l_ptr = r_ptr + 1
            r_ptr = max_jump

            num_jmps += 1
        
        return num_jmps
