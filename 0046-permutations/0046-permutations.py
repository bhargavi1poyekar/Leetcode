class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []
        def backtrack(arr):
            if len(arr) == len(nums):
                permutations.append(arr[:])
                return 
            
            for num in nums:
                if num not in arr:
                    arr.append((num))
                    backtrack(arr)
                    arr.pop()

        backtrack([])
        return permutations
        