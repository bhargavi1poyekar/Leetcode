class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        alpha_char = [ch for ch in s if ch.isalpha()]
        reverse = []
        
        for ch in s:
            if ch.isalpha():
                reverse.append(alpha_char.pop())
            else:
                reverse.append(ch)
        
        return ''.join(reverse)

        