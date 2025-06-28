class Solution:
    def jump(self, nums: List[int]) -> int:
        
        l = 0
        r = 0
        n = len(nums)
        jmps = 0

        while r < n-1:
            max_jmp = 0
            for i in range(l, r+1):
                max_jmp = max(max_jmp, i + nums[i])
            
            l = r
            r = max_jmp
            jmps += 1
        
        return jmps

        