class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        '''
        Understand:

        given -> s and k 
        return max vowel chars in any sub of length k. 

        Match:
        fixed length sliding window. 

        Plan:
        first fill the substring till length k. 
        inc the vowel count if any. 

        update max vowel count. 

        Now after k, inc left and right. 
        and adjust vowel count accpdingly. 

        At every point. udpate the max vowel count. 
        '''

        left = 0
        vowel_count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        max_vowel = 0

        for i in range(k):
            if s[i] in vowels:
                vowel_count += 1
        
        max_vowel = max(max_vowel, vowel_count)

        for right in range(k, len(s)):
            if s[right] in vowels:
                vowel_count += 1
            if s[left] in vowels:
                vowel_count -= 1

            left += 1
            
            max_vowel = max(max_vowel, vowel_count)
        
        return max_vowel

        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''