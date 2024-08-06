class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t)>len(s): return ""

        t_freq = Counter(t)
        distinct_t = len(t_freq)

        win_freq = Counter()

        min_left = 0
        min_right = 0

        match = 0
        left = 0
        min_length = float('inf')
        

        for right in range(len(s)):
            win_freq[s[right]] += 1

            if t_freq[s[right]] == win_freq[s[right]]:
                match += 1
            
            while distinct_t == match:
                if right - left + 1 < min_length:
                    min_left = left
                    min_right = right
                    min_length = right - left + 1

                if t_freq[s[left]] == win_freq[s[left]]:
                    match -= 1 
                
                win_freq[s[left]] -= 1
                left += 1
        
        return s[min_left:min_right+1] if min_length != float('inf') else ""




        