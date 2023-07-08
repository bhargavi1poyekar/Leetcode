class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]
        operators=['+','-','/','*']
        for tok in tokens:

            if tok in operators:
                
                int1=stack.pop()
                int2=stack.pop()

                if tok=='+':
                    stack.append(int2+int1)
                elif tok=='*':
                    stack.append(int2*int1)
                elif tok=='/':
                    stack.append(int(int2/int1))
                else:
                    stack.append(int(int2-int1))
            
            else:
                stack.append(int(tok))
        
        return stack[0]

