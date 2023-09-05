class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s)<=1:
            return len(s)
        
        max_len=0
        hash={}
        left=0
        for right in range(len(s)):
            if s[right] in hash:
                left=max(left,hash[s[right]])

            max_len=max(max_len,right-left+1)
            hash[s[right]]=right+1
        
        # max_len=max(max_len,right-left)
        return max_len
            
