class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s)==0:
            return 0
        
        left=0
        hash_idx={}
        max_len=0

        for right in range(len(s)):
            if s[right] in hash_idx:
                left=max(left,hash_idx[s[right]])

            hash_idx[s[right]]=right+1
            max_len=max(max_len,right-left+1)
        
        return max_len
        

        