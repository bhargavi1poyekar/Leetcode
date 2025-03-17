class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtrack(curr, i, currsum):
            if len(curr) == k and currsum == n:
                ans.append(curr[:])
                return 
            
            for j in range(i+1, 10):
                if currsum + j <= n:
                    curr.append(j)
                    backtrack(curr, j, currsum + j)
                    curr.pop()
        
        ans = []
        backtrack([], 0, 0)
        return ans
