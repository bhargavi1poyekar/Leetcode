class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        longest_cons_count = 0

        for num in nums:
            if num-1 not in num_set:
                curr_seq_count = 1
                while num+1 in num_set:
                    curr_seq_count+=1
                    num = num+1
                longest_cons_count = max(longest_cons_count, curr_seq_count)
        
        return longest_cons_count


