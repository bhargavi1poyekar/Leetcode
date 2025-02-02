class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        stack = [i for i in s if i.isalpha()]

        rev = []
        for ch in s:
            if ch.isalpha(): 
                rev.append(stack.pop())
            else:
                rev.append(ch)
        
        return ''.join(rev)