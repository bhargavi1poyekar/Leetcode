class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        max_length = 0
        index_hash = {}

        for right in range(len(s)):
            if s[right] in index_hash:
                left = max(left, index_hash[s[right]])
                
            index_hash[s[right]] = right + 1
            max_length = max(max_length, right - left + 1)
        
        return max_length

