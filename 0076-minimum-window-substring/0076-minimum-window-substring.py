class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_freq = Counter(t)
        window_freq = Counter()

        min_length = float('inf')
        min_left = 0
        min_right = 0
        left = 0

        match_count = 0

        for right in range(len(s)):
            window_freq[s[right]] += 1

            if window_freq[s[right]] == t_freq[s[right]]:
                match_count += 1

            # print(match_count, len(t_freq))
            # print(window_freq)

            while match_count == len(t_freq):
                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    min_left = left
                    min_right = right

                if window_freq[s[left]] == t_freq[s[left]]:
                    match_count -= 1

                window_freq[s[left]] -= 1
                left += 1

        # print(min_length, min_left, min_right)
        # print(s[min_left:min_right+1])
        if min_length == float('inf'):
            return ''
        return s[min_left:min_right + 1]

             
