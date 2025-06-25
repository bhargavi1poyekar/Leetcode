class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(i, arr):
            if i > len(nums):
                return 
            subsets.append(arr[:])

            for j in range(i, len(nums)):
                if j != i and nums[j] == nums[j-1]:
                    continue
                arr.append(nums[j])
                backtrack(j+1, arr)
                arr.pop()
        
        nums.sort()
        subsets = []
        backtrack(0, [])
        return subsets