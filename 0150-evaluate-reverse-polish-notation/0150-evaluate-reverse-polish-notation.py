class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        Understand:

        Given -> arr of tokens. -> represent arithmetic expression.   

        Evaluate and return value of expression. 

        valid ops -> -, +, *, / 

        operand -> int or another expression. 

        division -> truncates toward zero. 
        no division by 0

        valid arithmetic expression. 

        Match: Stack -> to get the previous executed expression. 

        Plan:

        if we get any operand, we put it in the stack. 
        if not, then we evaluate by popping last 2 elements of the stack. and performing that operation, and then adding the value back to stack. 
        '''

        stack = []
        operators = ('*', '+', '/', '-')

        for ch in tokens:
            if ch not in operators:
                stack.append(int(ch))
            elif ch == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num1 + num2))
            elif ch == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 - num1))
            elif ch == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num1 * num2))
            elif ch == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))

        return stack[-1]

        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
