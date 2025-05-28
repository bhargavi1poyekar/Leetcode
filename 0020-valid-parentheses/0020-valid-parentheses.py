class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        bracket_match = {
            '{':'}',
            '[':']',
            '(':')'
            }
        
        for ch in s:
            if ch in bracket_match:
                stack.append(bracket_match[ch])
            else:
                if stack and stack[-1] == ch:
                    stack.pop()
                else:
                    return False
        
        if not stack: 
            return True
        return False