class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        ls=[0 for i in range(len(nums)+1)]
        
        for i in range(1,len(ls)):
            ls[i]=ls[i-1]+nums[i-1]
        
        for j in range(n):
            if ls[j]==ls[n]-ls[j+1]:
                return j
        if ls[n-1]==0:
            return n-1
        else:
            return -1