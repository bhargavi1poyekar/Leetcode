class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        max_length = 0
        hash_idx = {}

        for right in range(len(s)):
            if s[right] in hash_idx:
                left = max(left, hash_idx[s[right]])
            
            max_length = max(right - left + 1, max_length)
            hash_idx[s[right]] = right + 1
        
        return max_length

        

        