class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # def dfs(left, right, s):
        #     if len(s) == n * 2:
        #         res.append(s)
        #         return 

        #     if left < n:
        #         dfs(left + 1, right, s + '(')

        #     if right < left:
        #         dfs(left, right + 1, s + ')')

        # res = []
        # dfs(0, 0, '')
        # return res

        def backtrack(current,left,right):
            if len(current) == 2 * n:
                answer.append("".join(current))
                return
            
            if left < n:
                current.append("(")
                backtrack(current,left + 1,right)
                current.pop()
            if right < left:
                current.append(")")
                backtrack(current,left,right + 1)
                current.pop()
        
        answer = []
        backtrack([],0,0)
        return answer


