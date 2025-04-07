class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dfs(nums, i, subset_sum) -> bool:
            # Base cases
            if subset_sum == 0:
                return True
            if i == 0 or subset_sum < 0:
                return False
            result = (dfs(nums, i - 1, subset_sum - nums[i - 1])
                    or dfs(nums, i - 1, subset_sum))
            return result

        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        n = len(nums)
        return dfs(tuple(nums), n - 1, subset_sum)