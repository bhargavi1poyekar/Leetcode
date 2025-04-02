class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtrack(i, curr, currsum):
            if currsum == n and len(curr) == k:
                ans.append(curr[:])
                return

            for num in range(i, 10):
                if currsum + num <= n:
                    curr.append(num)
                    backtrack(num + 1, curr, currsum + num)
                    curr.pop()
        
        ans = []
        backtrack(1, [], 0)
        return ans

