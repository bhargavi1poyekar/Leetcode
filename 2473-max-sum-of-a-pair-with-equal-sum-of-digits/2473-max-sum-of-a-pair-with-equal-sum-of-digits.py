class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        maxsum=-1
        digsum_hash={}
        for num in nums:
            digsum=0
            rem=0
            num_org=num
            while(num):
                rem=num%10
                digsum+=rem
                num=num//10
            # print(digsum, digsum_hash, maxsum)
            if digsum in digsum_hash:
                maxsum=max(maxsum,num_org+digsum_hash[digsum])
                digsum_hash[digsum]=max(digsum_hash[digsum],num_org)
            
            else:
                digsum_hash[digsum]=num_org
        
        return maxsum 