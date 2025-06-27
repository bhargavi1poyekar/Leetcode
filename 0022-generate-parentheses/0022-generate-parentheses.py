class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        valid = []
        def backtrack(arr, left, right):
            if len(arr) == n*2:
                valid.append(''.join(arr))
                return 

            if left < n:
                arr.append('(')
                backtrack(arr, left+1, right)
                arr.pop()

            if right < left:
                arr.append(')')
                backtrack(arr, left, right+1)
                arr.pop()

        backtrack([], 0, 0)
        return valid