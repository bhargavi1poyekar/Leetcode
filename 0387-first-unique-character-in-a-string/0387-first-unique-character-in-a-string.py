class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        s_count = {}

        for ch in s:
            s_count[ch] = s_count.get(ch, 0) + 1
        
        for i, ch in enumerate(s):
            if s_count[ch] == 1:
                return i
        
        return -1