class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        hash_count=Counter()

        total_count=0
        for i in range(len(nums)):
            if nums[i] in hash_count:
                total_count+=hash_count[nums[i]]
                hash_count[nums[i]]+=1
            else:
                hash_count[nums[i]]=1
        
        return total_count
            