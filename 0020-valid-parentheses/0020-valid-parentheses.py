class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket = {'(':')', '{':'}', '[':']'}
        stack = []

        for brack in s:
            if brack in bracket:
                stack.append(bracket[brack])
            else:
                if stack:
                    if brack == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        return len(stack) == 0