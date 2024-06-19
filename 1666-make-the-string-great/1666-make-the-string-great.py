class Solution:
    def makeGood(self, s: str) -> str:

        stack = []

        for ch in s:
            if stack:
                if ch != stack[-1] and ch.lower() == stack[-1].lower():
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        
    
        return ''.join(stack)