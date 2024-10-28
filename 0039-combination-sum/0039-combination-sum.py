class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(curr_path, curr_sum, i):
            if curr_sum == target:
                ans.append(curr_path[:])
                return
            
            for j in range(i, len(candidates)):
                num = candidates[j]
                if curr_sum + num <= target:
                    curr_path.append(candidates[j])
                    backtrack(curr_path, curr_sum + num, j)
                    curr_path.pop()
        
        ans = []
        backtrack([], 0, 0)
        return ans
