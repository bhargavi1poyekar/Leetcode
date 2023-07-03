class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        stack1=[]
        stack2=[]
        for i in s:
            # print(stack1)
            if i=='#' and stack1:
                stack1.pop()
            elif i!='#':
                stack1.append(i)

        
        for i in t:
            # print(stack2)
            if i=='#' and stack2:
                stack2.pop()
            elif i!='#':
                stack2.append(i)
        
        return stack1==stack2
        

        
        


