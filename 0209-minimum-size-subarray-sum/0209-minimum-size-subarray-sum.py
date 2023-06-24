class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums)<target:
            return 0
        if target in nums:
            return 1
        
        left=0
        
        min_length=len(nums)
        winsum=0

        for right in range(len(nums)):
            winsum+=nums[right]

            while(winsum>=target):
                min_length=min(min_length,right-left+1)
                winsum-=nums[left]
                left+=1
            

        return min_length






            

        