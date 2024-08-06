class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        max_freq_char = 0
        max_len = 0

        freq = Counter()

        for right in range(len(s)):
            freq[s[right]] += 1
            if freq[s[right]] >= freq[max_freq_char]:
                max_freq_char = s[right]
            
            curr_len = right - left + 1

            if curr_len - freq[max_freq_char] > k:
                freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right- left+1)

        return max_len 
