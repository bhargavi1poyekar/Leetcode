class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_positive_sum = 0
        max_negative_sum = 0

        curr_positive_sum = 0
        curr_negative_sum = 0

        for num in nums:
            curr_positive_sum = max(curr_positive_sum + num, num)
            max_positive_sum = max(max_positive_sum, curr_positive_sum)

            curr_negative_sum = min(curr_negative_sum + num, num)
            max_negative_sum = min(max_negative_sum, curr_negative_sum)

        return max(max_positive_sum, abs(max_negative_sum))