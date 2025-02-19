class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def backtrack(curr,last):
            if len(curr) == n:
                ans.append(''.join(curr))
                return
        
            for ch in ['a','b','c']:
                if ch !=last:
                    curr.append(ch)
                    backtrack(curr,ch)
                    curr.pop()
            
        ans = []
        backtrack([],'')
        return ans[k-1] if k<=len(ans) else ""