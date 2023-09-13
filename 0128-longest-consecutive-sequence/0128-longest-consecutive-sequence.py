class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set=set(nums)
        max_len=0
        for n in nums_set:
            count=1
            num=n
            # print()num
            if num-1 not in nums_set:
                while num+1 in nums_set:
                    count+=1
                    num+=1
                max_len=max(max_len,count)
        
        return max_len

        