class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]
        for tok in tokens:
            

            if tok=='+' and stack:
                op1=int(stack.pop())
                op2=int(stack.pop())
                stack.append(op1+op2)
            elif tok=='*' and stack:
                op1=int(stack.pop())
                op2=int(stack.pop())
                stack.append(op1*op2)
            elif tok=='-' and stack:
                op1=int(stack.pop())
                op2=int(stack.pop())
                stack.append(op2-op1)
            elif tok=='/' and stack:
                op1=int(stack.pop())
                op2=int(stack.pop())
                stack.append(int(op2/op1))
            else:
                stack.append(tok)
            
        return(int(stack[-1]))

