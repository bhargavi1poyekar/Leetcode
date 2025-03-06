class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        longest_seq = 0

        for num in num_set:
            # curr_len = 1
            if (num - 1) not in num_set:
                curr_len = 1
                while num + curr_len in num_set:
                    curr_len += 1
                    # num = num + 1
                longest_seq = max(longest_seq, curr_len)
        
        return longest_seq

        # num_set = set(nums)
        # longest = 0

        # for n in num_set:
        #     if n - 1 not in num_set:
        #         length = 1

        #         while n + length in num_set:
        #             length += 1
                
        #         longest = max(longest, length)
        
        # return longest

