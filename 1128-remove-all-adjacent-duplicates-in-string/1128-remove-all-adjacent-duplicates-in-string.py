class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack=[]

        for i in s:
            if stack and i==stack[-1]:
                while stack and i==stack[-1]:
                    stack.pop()
            elif stack and i!=stack[-1]:
                stack.append(i)
            else:
                stack.append(i)
        
        return ''.join(stack)
            


                



        