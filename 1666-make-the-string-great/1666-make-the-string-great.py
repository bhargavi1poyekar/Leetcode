class Solution:
    def makeGood(self, s: str) -> str:
        
        stack=[]
        for i in s:
            if stack and i!=stack[-1] and i.lower()==stack[-1].lower():
                stack.pop()
            else:
                stack.append(i)
        
        return ''.join(stack)