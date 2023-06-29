class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        sums=collections.Counter()
        sums[0]=1
        count=0
        pre_sum=0
        for right in range(len(nums)):
            pre_sum+=nums[right]
            # print(pre_sum,count,sums)
            if pre_sum-goal in sums:
                count+=sums[pre_sum-goal]
            
            sums[pre_sum]+=1
        return count