class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hash={}

        left=0
        max_len=0
        for right in range(len(s)):
            
            if s[right] in hash:
                left=max(left,hash[s[right]])
            max_len=max(max_len,right-left+1)
            hash[s[right]]=right+1
        
        return max_len

        

        