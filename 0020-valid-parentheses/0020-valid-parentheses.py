class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]
        pairs={'(':')','{':'}','[':']'}

        for i in s:
            if i in pairs:
                stack.append(pairs[i])
            else:
                if not stack:
                    return False
                elif i==stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return not stack 
                
                
