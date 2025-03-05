class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = ['']
        num = 0

        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i] == '[':
                stack.append(num)
                num = 0
                stack.append('')
            
            elif s[i] == ']':
                str1 = stack.pop()
                count = stack.pop()
                str2 = stack.pop()
                stack.append(str2 + str1 * count)
            
            else:
                stack[-1] += s[i]
        
        return stack[-1]