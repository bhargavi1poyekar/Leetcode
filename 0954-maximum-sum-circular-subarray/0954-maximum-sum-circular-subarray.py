class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Helper function to find max subarray sum using Kadane's algorithm
        def kadane(arr):
            current_max = max_sum = arr[0]
            for num in arr[1:]:
                current_max = max(num, current_max + num)
                max_sum = max(max_sum, current_max)
            return max_sum
        
        # Case 1: Maximum Sum of Non-Circular Subarray
        max_kadane = kadane(nums)
        
        # Case 2: Maximum Sum of Circular Subarray
        total_sum = sum(nums)
        # Invert array for minimum subarray sum
        min_sum = kadane([-num for num in nums])
        
        # Handle the case where all numbers are negative
        if total_sum == -min_sum:
            return max_kadane
        
        # Result is the maximum of both cases
        return max(max_kadane, total_sum + min_sum)  # total_sum + min_sum is total_sum - (-min_sum)
