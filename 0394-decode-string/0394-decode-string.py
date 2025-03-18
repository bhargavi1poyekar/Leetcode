class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = [""]
        op = 0
        curr_str = ""
        for ch in s:
            if ch.isalpha():
                stack[-1] += ch
            elif ch == '[':
                stack.append(op)
                stack.append("")
                op = 0
            elif ch == ']':
                string = stack.pop()
                count = stack.pop()
                stack[-1] += string*count    
            else:
                op = op*10 + int(ch)
        
        return stack[-1]

        
        