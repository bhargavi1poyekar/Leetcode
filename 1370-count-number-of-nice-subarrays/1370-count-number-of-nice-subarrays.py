class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        hash=collections.Counter()
        hash[0]=1
        odd_count=0
        count=0
        
        for i in nums:
            if i%2==1:
                odd_count+=1
            count+=hash[odd_count-k]
            hash[odd_count]+=1
        
        return count