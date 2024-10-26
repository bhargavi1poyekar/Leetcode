class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        res = 0
        op = 0
        sign = 1

        for i in s:
            if i == '(':
                stack.append(res)
                stack.append(sign)

                res = 0
                sign = 1
            
            elif i.isdigit():
                op = op*10 + int(i)
            
            elif i == '+':
                res += sign * op
                sign = 1
                op = 0
            elif i == '-':
                res += sign * op
                sign = -1
                op = 0
            elif i ==')':
                res += sign * op
                res *= stack.pop() # sign
                res += stack.pop() # prev result
                op = 0

        return res + sign * op
    
