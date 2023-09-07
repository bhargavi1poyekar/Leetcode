class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_hash=Counter()
        prefix_hash[0]=1
        count=0
        prefix_sum=0
        for i in nums:
            prefix_sum+=i
            count+=prefix_hash[prefix_sum-k]
            prefix_hash[prefix_sum]+=1
        
        return count