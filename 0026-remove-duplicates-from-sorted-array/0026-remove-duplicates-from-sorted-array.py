class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        start = 0
        end = 0

        while start < len(nums) and end < len(nums):
            if nums[end] == nums[start]:
                end += 1
            else:
                nums[start+1] = nums[end]
                start += 1
        
        return start+1
        