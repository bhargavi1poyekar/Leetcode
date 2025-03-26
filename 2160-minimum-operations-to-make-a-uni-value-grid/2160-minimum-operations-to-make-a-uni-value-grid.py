class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        nums = []

        for row in grid:
            for num in row:
                nums.append(num)
        
        nums.sort()

        length = len(nums)
        median = nums[length // 2]
        min_op = 0

        for num in nums:
            if num % x != median % x:
                return -1
            min_op += abs(median - num) // x

        return min_op
