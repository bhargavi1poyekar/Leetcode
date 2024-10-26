class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        max_length = 0
        for num in nums:
            curr_num = num
            if num - 1 not in nums_set:
                count = 1
                while num + 1 in nums_set:
                    count += 1
                    num = num + 1
                max_length = max(max_length, count)
        
        return max_length

