class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(i, curr):
            if sum(curr) == target:
                ans.append(curr[:])
                return 
            if sum(curr) > target:
                return 
            
            for num in range(i, len(candidates)):
                curr.append(candidates[num])
                backtrack(num, curr)
                curr.pop()
        
        ans = []
        backtrack(0, [])
        return ans
