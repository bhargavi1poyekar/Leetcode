class Solution:
    def isValid(self, s: str) -> bool:
        
        matching_brackets = {
            '{':'}',
            '[':']',
            '(':')'
        }

        stack = []

        for bracket in s:

            if bracket in matching_brackets:
                stack.append(matching_brackets[bracket])
            else:
                if stack and stack[-1] == bracket:
                    stack.pop()
                else:
                    return False
            
        if not stack:
            return True
        return False

            
