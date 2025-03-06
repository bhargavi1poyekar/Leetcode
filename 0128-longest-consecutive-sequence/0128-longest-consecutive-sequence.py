class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # num_set = set(nums)
        # longest_seq = 0

        # for num in nums:
        #     # curr_len = 1
        #     if (num - 1) not in num_set:
        #         curr_len = 1
        #         while (num + 1) in num_set:
        #             curr_len += 1
        #             num = num + 1
        #         longest_seq = max(longest_seq, curr_len)
        
        # return longest_seq

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

