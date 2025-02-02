class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = ['+', '-', '/', '*']
        stack = []

        for tok in tokens:
            # print(stack)
            if tok in operators:
                num1 = stack.pop()
                num2 = stack.pop()

                if tok == '+':
                    stack.append(int(num1 + num2))
                elif tok == '-':
                    stack.append(int(num2 - num1))
                elif tok == '*':
                    stack.append(int(num1 * num2))
                else:
                    stack.append(int(num2 / num1))
            else:
                stack.append(int(tok))
        
        return stack[-1]