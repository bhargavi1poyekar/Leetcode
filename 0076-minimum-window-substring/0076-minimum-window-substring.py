class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        min_length = float('inf')
        min_right = 0
        min_left = 0
        win_freq = Counter()
        t_freq = Counter(t)
        distinct_t = len(t_freq)
        match_count = 0

        left = 0

        for right in range(len(s)):
            win_freq[s[right]] += 1
            if t_freq[s[right]] == win_freq[s[right]]:
                match_count += 1
            
            while match_count == distinct_t:
                if min_length > right - left + 1:
                    min_length = right - left + 1
                    min_left = left
                    min_right = right
                
                if t_freq[s[left]] == win_freq[s[left]]:
                    match_count -= 1
                
                win_freq[s[left]] -= 1
                left += 1
        
        if min_length == float('inf'): return ''
        else:
            return s[min_left: min_right + 1]
                

