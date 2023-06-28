class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        hash=collections.Counter()
        hash[0]=1
        count=0
        prefix_sum=0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            count+=hash[prefix_sum-k]
            hash[prefix_sum]+=1
        return count
            
            
