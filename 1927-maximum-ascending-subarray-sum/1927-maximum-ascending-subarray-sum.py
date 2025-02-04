class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        curr_sum = nums[0]

        left = 0
        for right in range(1, len(nums)):
            if nums[right] <= nums[right-1]:
                left = right
                curr_sum = nums[right]
            else:
                curr_sum += nums[right]
            
            max_sum = max(max_sum, curr_sum)
        
        return max_sum

                
         
