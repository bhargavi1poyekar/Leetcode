class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        left_sum = 0
        total_sum = sum(nums)
        valid_split = 0

        for i in range(len(nums)-1):
            left_sum += nums[i]
            if left_sum >= total_sum - left_sum:
                # print(num)
                valid_split += 1
        
        return valid_split
