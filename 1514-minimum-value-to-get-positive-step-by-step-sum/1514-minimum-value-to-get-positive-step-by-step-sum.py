class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        min_sum=0
        prefix_sum=0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            min_sum=min(prefix_sum,min_sum)
        
        if min_sum==0:
            return 1
        else:
            return abs(min_sum)+1
