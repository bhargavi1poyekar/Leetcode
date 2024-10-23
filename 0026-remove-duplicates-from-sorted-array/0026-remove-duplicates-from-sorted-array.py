class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        start = 0
        end = 0
        n = len(nums)
        while start < n and end < n:
            if nums[start] == nums[end]:
                end += 1
            else:
                nums[start+1] = nums[end]
                start += 1

        return start+1