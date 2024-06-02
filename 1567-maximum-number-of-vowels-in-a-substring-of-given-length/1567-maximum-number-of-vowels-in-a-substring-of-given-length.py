class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        left = 0
        max_length = 0
        curr_vowel_length = 0  
        vowels = ['a', 'e', 'i', 'o', 'u']

        for right in range(k):
            if s[right] in vowels:
                curr_vowel_length +=1

        max_length = curr_vowel_length    
        
        for right in range(k, len(s)):
            if s[right] in vowels:
                curr_vowel_length += 1
            
            if s[left] in vowels:
                curr_vowel_length -= 1
            
            left += 1
            max_length = max(max_length, curr_vowel_length)
        
        return max_length
        