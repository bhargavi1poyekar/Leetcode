class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(i, arr):
            if i > len(nums):
                return 
            
            subsets.append(arr[:])

            for j in range(i, len(nums)):
                arr.append(nums[j])
                backtrack(j+1, arr)
                arr.pop()
        
        subsets = []
        backtrack(0, [])
        return subsets
