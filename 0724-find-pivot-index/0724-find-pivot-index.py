class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total_sum = sum(nums)
        curr_sum = 0

        for i in range(len(nums)):
            right_sum = total_sum - curr_sum - nums[i]
            if right_sum == curr_sum:
                return i
            curr_sum += nums[i]
        
        return -1

