class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]
        operators=['+','-','/','*'] # Valid operators 
        for tok in tokens:

            if tok in operators: # if token is operator
                # take out the top 2 integer values
                int1=stack.pop() 
                int2=stack.pop()

                if tok=='+': 
                    stack.append(int2+int1)
                elif tok=='*':
                    stack.append(int2*int1)
                elif tok=='/':
                    stack.append(int(int2/int1)) # value closer to 0
                else:
                    stack.append(int(int2-int1))
            
            else:
                stack.append(int(tok)) # if token is integer
        
        return stack[0] # return final ans

