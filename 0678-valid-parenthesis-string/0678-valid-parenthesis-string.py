class Solution:
    def checkValidString(self, s: str) -> bool:
        
        open_stack = []
        star_stack = []

        for i, ch in enumerate(s):
            if ch == '(':
                open_stack.append(i)
            elif ch == '*':
                star_stack.append(i)
            else:
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
        if len(star_stack) < len(open_stack):
            return False
        
        while open_stack:
            if open_stack[-1] > star_stack[-1]:
                return False
            open_stack.pop()
            star_stack.pop()
        
        return True