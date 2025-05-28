class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = ['+', '-', '*', '/']

        stack = []

        for tok in tokens:
            if tok not in operators:
                stack.append(int(tok))
            else:
                if tok == '+':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(int(num1 + num2))
                elif tok == '*':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(int(num1 * num2))
                elif tok == '-':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(int(num2 - num1))
                else:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(int(num2 / num1))
        
        return stack[-1]