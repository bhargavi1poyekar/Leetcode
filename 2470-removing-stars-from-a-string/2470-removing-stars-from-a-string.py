class Solution:
    def removeStars(self, s: str) -> str:

        stack=[]

        for i in s:
            if stack and i=='*': # remove closest non star char 
                stack.pop()
            else: # add all other elements other than star
                stack.append(i)

        return(''.join(stack))
        
