class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vowels = 0
        num_vowels = 0

        for i in range(k):
            if s[i] in vowels:
                num_vowels += 1
        
        max_vowels = num_vowels

        left = 0
        for right in range(k, len(s)):
            if s[right] in vowels:
                num_vowels += 1

            if s[left] in vowels:
                num_vowels -= 1
            
            left += 1
            max_vowels = max(max_vowels, num_vowels)
        
        return max_vowels