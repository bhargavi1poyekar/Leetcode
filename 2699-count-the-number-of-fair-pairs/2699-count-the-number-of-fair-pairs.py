class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        def lower_bound(nums: List[int], value: int) -> int:
            left = 0
            right = len(nums) - 1
            result = 0
            while left < right:
                sum = nums[left] + nums[right]
                # If sum is less than value, add the size of window to result and move to the
                # next index.
                if sum < value:
                    result += right - left
                    left += 1
                else:
                    # Otherwise, shift the right pointer backwards, until we get a valid window.
                    right -= 1
            return result
            
        nums.sort()
        return lower_bound(nums, upper + 1) - lower_bound(nums, lower)
        
        