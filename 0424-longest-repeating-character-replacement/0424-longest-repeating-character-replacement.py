class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_length = 0
        left = 0
        freq = Counter()
        max_char = s[0]


        for right in range(len(s)):
            freq[s[right]] += 1
            if freq[s[right]] > freq[max_char]:
                max_char = s[right]

            window_size = right - left + 1 
            if window_size - freq[max_char] > k:
                freq[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right -left + 1)
        
        return max_length

        