class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]
        brackets={'(':')','{':'}','[':']'}

        for i in s:
            if i in brackets:
                stack.append(brackets[i])
            else:
                if not stack:
                    return False
                elif i==stack[-1]:
                    stack.pop()
                else:
                    return False 
        
        return True if not stack else False


                
                
                
