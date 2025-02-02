class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def backspace(s):
            stack = []

            for ch in s:
                if ch != '#':
                    stack.append(ch)
                else:
                    if stack:
                        stack.pop()
            
            return ''.join(stack)
        
        return backspace(s) == backspace(t)
                