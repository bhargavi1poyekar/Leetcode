class Solution:
    def jump(self, nums: List[int]) -> int:

        l=0
        r=0
        jmp=0

        while(r<len(nums)-1):
            
            max_jmp=0
            for i in range(l,r+1):
                max_jmp=max(max_jmp,i+nums[i])
            
            l=r+1
            r=max_jmp
            jmp+=1
        return jmp
