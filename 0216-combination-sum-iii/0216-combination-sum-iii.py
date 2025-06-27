class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtrack(i, curr, currsum):
            if currsum == n and len(curr) == k:
                ans.append(curr[:])
                return
            
            if currsum > n:
                return 

            for num in range(i, 10):
                curr.append(num)
                backtrack(num + 1, curr, currsum + num)
                curr.pop()
        
        ans = []
        backtrack(1, [], 0)
        return ans

