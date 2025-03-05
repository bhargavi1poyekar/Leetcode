class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = {'+', '-', '/', '*'}

        stack = []

        for tok in tokens:
            # print(stack)
            if tok not in operators: 
                stack.append(int(tok))
            
            elif tok == '+':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op1 + op2))
            
            elif tok == '-':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op2 - op1))
            
            elif tok == '*':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op1 * op2))

            elif tok == '/':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op2 / op1))
        
        return(stack[-1])