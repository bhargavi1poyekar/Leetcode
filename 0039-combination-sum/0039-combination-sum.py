class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(i, arr):
            if sum(arr) == target:
                combinations.append(arr[:])
                return
            
            if sum(arr) > target:
                return 
            
            for j in range(i, len(candidates)):
                arr.append(candidates[j])
                backtrack(j, arr)
                arr.pop()
        
        combinations = []
        backtrack(0, [])
        return combinations