class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        char_freq = Counter()
        left = 0
        max_length = 0
        max_char = s[0]

        for right in range(len(s)):
            char_freq[s[right]] += 1
        
            if char_freq[s[right]] >= char_freq[max_char]:
                max_char = s[right]
            
            curr_length = right - left + 1

            if curr_length - char_freq[max_char] > k:
                char_freq[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        
        return max_length

