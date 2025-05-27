class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        if not s:
            return 0

        max_freq_char = s[0]
        freq_char = Counter()
        max_length = 0
        max_freq = 0
        left = 0

        for right in range(len(s)):
            freq_char[s[right]] += 1

            if freq_char[s[right]] >= max_freq:
                max_freq_char = s[right]
                max_freq = freq_char[s[right]]

            curr_length = right - left + 1
            if curr_length - max_freq > k:
                freq_char[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
             
