import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        
        curr_sum = sum(nums)
        targetSum = sum(nums) / 2
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        num_op = 0
        # print(curr_sum)
        while curr_sum > targetSum:
            max_element = heapq.heappop(nums)
            half = max_element / 2
            curr_sum += half
            heapq.heappush(nums, half)
            num_op += 1

        return num_op

