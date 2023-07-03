class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]
        pairs={'(':')','{':'}','[':']'}

        for i in s:
            if i in pairs:
                stack.append(pairs[i])
            elif not stack:
                return False
            else:
                if i==stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False
                
                
