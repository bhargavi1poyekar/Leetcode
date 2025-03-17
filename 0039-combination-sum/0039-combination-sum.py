class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(i, curr, currsum):
            if currsum == target:
                ans.append(curr[:])
                return 
            
            for j in range(i, len(candidates)):
                num = candidates[j]
                if currsum + num <= target:
                    curr.append(num)
                    backtrack(j, curr, currsum+num)
                    curr.pop()
        
        ans = []
        backtrack(0, [], 0)
        return ans
