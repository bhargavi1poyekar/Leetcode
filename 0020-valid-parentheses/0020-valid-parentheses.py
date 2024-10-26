class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {
            '{':"}",
            '[':']',
            '(':')'
        }
        stack = []
        for bracket in s:
            if bracket in brackets:
                stack.append(brackets[bracket])
            else:
                if stack and bracket == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
