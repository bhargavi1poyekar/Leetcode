class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = (['+', '*', '/', '-'])
        stack = []
        for tok in tokens:
            if tok not in operators:
                stack.append(tok)
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())

                if tok == '+':
                    stack.append(int(num1+num2))
                elif tok == '*':
                    stack.append(int(num1*num2))
                elif tok == '-':
                    stack.append(int(num2-num1))
                else:
                    stack.append(int(num2 / num1))

        return int(stack[-1])
