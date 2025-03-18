class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        used_bits = 0  # Tracks bits used in current window
        left = 0  # Start position of current window
        max_length = 0  # Length of longest nice subarray found

        for right in range(len(nums)):
            # If current number shares bits with window, shrink window from left
            # until there's no bit conflict
            while used_bits & nums[right] != 0:
                used_bits ^= nums[left]  # Remove leftmost element's bits
                left += 1  # Shrink window from left

            # Add current number to the window
            used_bits |= nums[right]

            # Update max length if current window is longer
            max_length = max(max_length, right - left + 1)

        return max_length