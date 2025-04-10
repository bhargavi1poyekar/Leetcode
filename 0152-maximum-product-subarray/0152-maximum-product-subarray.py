class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_prod = nums[0]
        min_prod = nums[0]
        largest_prod = max_prod

        for i in range(1, len(nums)):
            num = nums[i]
            temp_max = max(num, max_prod*num, min_prod*num)
            min_prod = min(num, min_prod*num, max_prod*num)

            max_prod = temp_max
            largest_prod = max(max_prod, largest_prod)

        return largest_prod    


