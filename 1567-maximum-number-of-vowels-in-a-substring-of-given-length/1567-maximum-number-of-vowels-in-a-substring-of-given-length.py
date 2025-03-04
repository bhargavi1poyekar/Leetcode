class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        left = 0
        vowel_count = 0
        max_vow_count = 0

        for right in range(k):
            if s[right] in vowels:
                vowel_count += 1
        
        max_vow_count = vowel_count

        for right in range(k, len(s)):
            if s[right] in vowels:
                vowel_count += 1
            
            if s[left] in vowels:
                vowel_count -= 1
            
            left += 1
            max_vow_count = max(max_vow_count, vowel_count)
        
        return max_vow_count
        
        