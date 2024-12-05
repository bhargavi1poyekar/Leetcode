class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        def backtrack(curr,i):
            
            if len(curr)==len(digits):
                print(curr)
                ans.append(''.join(curr))
                return
            
            for letter in hash[digits[i]]:
                curr.append(letter)
                backtrack(curr, i+1)
                curr.pop()
            
        hash={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        ans=[]
        backtrack([],0)
        return ans

