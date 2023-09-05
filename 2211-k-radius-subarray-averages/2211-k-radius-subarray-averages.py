class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        prefix=[]
        prefix.append(0)
        for i in range(len(nums)):
            prefix.append(prefix[i]+nums[i])
        
        num=2*k+1

        avg=[-1]*len(nums)
        for i in range(len(nums)):
            if i-k>=0 and i+k<len(nums):
                avg[i]=int((prefix[i+k+1]-prefix[i-k])/num)

        return avg

        
