class Solution:
    def decodeString(self, s: str) -> str:

        stack = ['']
        num = 0

        for ch in s:
            if ch == '[':
                stack.append(num)
                stack.append('')
                num = 0
            elif ch == ']':
                string = stack.pop()
                k = stack.pop()
                stack[-1] += k*string
            elif ch.isalpha():
                stack[-1] += ch
            else:
                num = num*10 + int(ch)
        
        return stack[-1]

        
