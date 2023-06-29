class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        left=0
        hash_index={}
        prefix_sum=[0]
        for i in range(0,len(nums)):
            prefix_sum.append(nums[i]+prefix_sum[i])
        # print(prefix_sum)

        max_sum=0
        # sum=0
        
        for right in range(len(nums)):
            # print(max_sum,right,left,hash_index,prefix_sum[right+1],prefix_sum[left])
            if nums[right] in hash_index:
                max_sum=max(max_sum,prefix_sum[right]-prefix_sum[left])
                left=max(left,hash_index[nums[right]])
            hash_index[nums[right]]=right+1
        
        # print(max_sum,right,left,hash_index, prefix_sum[right+1], prefix_sum[left])
        max_sum=max(max_sum,prefix_sum[right+1]-prefix_sum[left])
        
        return(max_sum)
        



