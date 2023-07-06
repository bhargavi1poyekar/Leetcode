class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]
        op=['+','/','-','*']
        for tok in tokens:
            if tok=='+' and stack:
                op1=stack.pop()
                op2=stack.pop()
                stack.append(op1+op2)
            elif tok=='*' and stack:
                op1=stack.pop()
                op2=stack.pop()
                stack.append(op1*op2)
            elif tok=='-' and stack:
                op1=stack.pop()
                op2=stack.pop()
                stack.append(op2-op1)
            elif tok=='/' and stack:
                op1=stack.pop()
                op2=stack.pop()
                stack.append(int(op2/op1))
            else:
                stack.append(int(tok))
            
        return(stack[-1])

