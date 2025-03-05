class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_match = {
            '[':']',
            '(':')',
            '{':'}'
        }

        stack = []

        for ch in s:
            if ch in bracket_match:
                stack.append(bracket_match[ch])
            else:
                if stack and stack[-1] == ch:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0