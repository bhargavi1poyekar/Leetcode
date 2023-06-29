class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        count=0
        hash_index={}

        for num in nums:
            if num in hash_index:
                count+=hash_index[num]
                hash_index[num]+=1
            else:
                hash_index[num]=1
            
        return count
