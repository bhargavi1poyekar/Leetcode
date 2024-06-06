class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_match = {
            '{':'}',
            '[':']',
            '(':')'
        }

        stack = []

        for bracket in s:
            if bracket in bracket_match:
                stack.append(bracket_match[bracket])
            else:
                if stack:
                    if stack[-1] == bracket:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        if not stack:
            return True
