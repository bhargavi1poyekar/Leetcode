class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = [""]
        op = 0

        for ch in s:
            if ch == ']':
                string = stack.pop()
                k = stack.pop()
                stack[-1] += k*string
            elif ch == '[':
                stack.append(op)
                stack.append("")
                op = 0
            elif ch.isalpha():
                stack[-1] += ch
            else:
                op = op*10 + int(ch)

        return stack[0]