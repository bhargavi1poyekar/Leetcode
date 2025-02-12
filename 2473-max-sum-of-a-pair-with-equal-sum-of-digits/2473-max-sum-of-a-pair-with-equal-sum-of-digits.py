class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        def sum_of_digits(num):
            sum = 0
            while(num):
                sum += num % 10
                num = num // 10
            return sum

        hash_sum = {}
        max_sum_of_nums = -1

        for i in range(len(nums)):
            digit_sum = sum_of_digits(nums[i])
            if digit_sum in hash_sum:
                j = hash_sum[digit_sum]
                num_sum = nums[i] + nums[j]
                max_sum_of_nums = max(max_sum_of_nums, num_sum)
                if nums[i] >= nums[j]:
                    hash_sum[digit_sum] = i
            else:
                hash_sum[digit_sum] = i
        
        return max_sum_of_nums
