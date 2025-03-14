import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        
        half_target = sum(nums) / 2
        curr_sum = sum(nums)
        oper = 0

        nums = [ -num for num in nums ]
        heapq.heapify(nums)

        while curr_sum > half_target:
            max_int = heapq.heappop(nums)
            oper += 1 
            half = max_int / 2
            curr_sum += half
            heapq.heappush(nums, half)
        
        return oper

