class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        min_length = float('inf')
        min_left = 0
        min_right = 0

        t_freq = Counter(t)
        win_freq = Counter()
        unique_t = len(t_freq)
        match_count = 0
        left = 0

        for right in range(len(s)):
            win_freq[s[right]] += 1
            
            if win_freq[s[right]] == t_freq[s[right]]:
                match_count += 1
            
            while match_count == unique_t:
                curr_length = right - left + 1
                if curr_length < min_length:
                    min_left = left
                    min_right = right
                    min_length = curr_length
                
                if win_freq[s[left]] == t_freq[s[left]]:
                    match_count -= 1
                
                win_freq[s[left]] -= 1
                left += 1
            
        if min_length != float('inf'):
            return s[min_left: min_right+1]
        else:
            return ""

