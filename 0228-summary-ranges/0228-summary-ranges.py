class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        intervals = []

        num_set = set(nums)

        for num in nums:
            curr_num = num
            if curr_num - 1 not in num_set:
                start = curr_num
                while curr_num + 1 in num_set:
                    curr_num += 1
                end = curr_num
                if start == end:
                    intervals.append(f'{start}')
                else:
                    intervals.append(f'{start}->{end}')
        return intervals

