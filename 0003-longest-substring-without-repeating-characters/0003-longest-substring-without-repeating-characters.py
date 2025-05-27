class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        last_index = {}
        left = 0

        max_length = 0

        for right in range(len(s)):
            if s[right] in last_index:
                left = max(left, last_index[s[right]])
            
            last_index[s[right]] = right + 1
            max_length = max(max_length, right - left + 1)
        
        return max_length
            

