class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        '''
        Understand:

        Given -> arr of pos int nums. and pos int target. 
        return min length of subarray whose sum >= target. 

        no subarray -> return 0

        Match:
        Sliding window -> variable length

        Plan:
        we keep adding new elements to window and sum. 
        once sum becomes >= target, we try to remove elements from left. And till the sum >= target, we update min length of window. 
        '''

        left = 0
        min_length = len(nums) + 1
        curr_sum = 0

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                min_length = min(min_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        # If no subarray sum greater than target, then min_length will be what we initialized. 
        return min_length if min_length != len(nums) + 1 else 0

        

        