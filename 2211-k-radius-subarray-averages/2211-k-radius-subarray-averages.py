class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if len(nums)<2*k:
            return [-1]*len(nums)
        
        total_count=2*k+1

        prefix_sum=[0]*(len(nums)+1)
        avgs=[-1]*len(nums)

        for i in range(len(nums)):
            prefix_sum[i+1]=prefix_sum[i]+nums[i]
        
        print(prefix_sum)
        
        for i in range(len(nums)):
            if i>=k and i<len(nums)-k:
                avgs[i]=(prefix_sum[i+k+1]-prefix_sum[i-k])//total_count
        
        return avgs