class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        prefix_sum=[0]*len(nums)
        prefix_sum[0]=nums[0]
        for i in range(1,len(nums)):
            prefix_sum[i]=nums[i]+prefix_sum[i-1]
        
        min_sum=min(prefix_sum)
        if min_sum<0:
            return abs(min_sum)+1
        else:
            return 1
