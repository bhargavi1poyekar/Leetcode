class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def backspace(str):

            stack = []

            for ch in str:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            
            return ''.join(stack)
        
        return backspace(s) == backspace(t)