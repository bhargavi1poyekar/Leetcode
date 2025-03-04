class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        left = 0
        curr_sum = 0
        max_sum = float('-inf')

        for right in range(k):
            curr_sum += nums[right]
        
        max_sum = curr_sum
        # print(curr_sum)

        for right in range(k, len(nums)):
            curr_sum += nums[right] - nums[left]
            # print(curr_sum)
            max_sum = max(max_sum, curr_sum)
            left += 1
        
        return max_sum / k
        
