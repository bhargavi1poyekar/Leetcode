class Solution:
    def reverseVowels(self, s: str) -> str:

        ptr1 = 0
        ptr2 = len(s)-1
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        while ptr1 < ptr2:
            if s[ptr1] in vowels and s[ptr2] in vowels:
                s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
                ptr1 += 1
                ptr2 -= 1
            if s[ptr2] not in vowels:
                ptr2 -= 1
            if s[ptr1] not in vowels:
                ptr1 += 1
        
        return ''.join(s)


        