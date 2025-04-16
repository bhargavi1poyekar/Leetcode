class Solution:
    def decodeString(self, s: str) -> str:
        '''
        Understand:

        Given -> encoded string
        k[encoded_string] -> encoded string -> repeated k times. k-> pos integer.

        input-> always valid. No white spaces. brackets are valid. No digits in that. 

        all chars -> lowercase. 

        Match: Stack -> to get the string to be repated, and how many times. 

        Plan:

        We have stack.

        While we have a digit -> we keep on creating the complete number. op = op*10 + num

        When we get [ open bracket -> we push the op to stack, and also push an empty string. 

        When we get a char -> we append it to top of stack

        When open bracket -> pop string first, then k. Multiple k with string, and append back to stack. 
        '''

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


            
        