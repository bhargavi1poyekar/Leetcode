class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_so_far = 1
        min_so_far = 1

        max_prod = float('-inf')

        for num in nums:
            max_temp = max(num, max_so_far*num, min_so_far*num)
            min_so_far = min(num, max_so_far*num, min_so_far*num)

            max_so_far = max_temp
            max_prod = max(max_prod, max_so_far)

        return max_prod