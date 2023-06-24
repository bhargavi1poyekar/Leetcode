class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        # if len(s)<=1:
        #     return len(s)

        hash={}
        left=0
        max_length=0
        for right in range(len(s)):
            
            if s[right] in hash:
               left=max(left,hash[s[right]])
            max_length=max(max_length,right-left+1)
            hash[s[right]]=right+1

            
        return max_length

        