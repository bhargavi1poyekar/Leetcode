class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        '''
        Given:
        circular int arra -> nums of lenght n
        return max possible sum of non empty sub of nums.

        Match: Greedy -> Kadane's ALgorithm
        '''

        def kadane(nums):

            max_sum = float('-inf')
            curr = 0
            for num in nums:
                curr = max(num, curr + num)
                max_sum = max(max_sum, curr)
            
            return max_sum
        
        max_sum = kadane(nums)
        neg_nums = [-num for num in nums]
        min_sum = kadane(neg_nums)

        total_sum = sum(nums)

        if total_sum == -min_sum:
            return max_sum
        
        return max(max_sum, total_sum + min_sum)
    