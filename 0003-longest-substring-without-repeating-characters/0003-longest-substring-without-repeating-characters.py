class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s)==0:
            return 0
        hash={}
        left=0
        max_len=0
        for right in range(len(s)):
            
            if s[right] in hash:
                max_len=max(max_len,right-left)
                left=max(left,hash[s[right]]+1)

            hash[s[right]]=right
            # print(left,right,max_len, hash)

        # print(left,right,max_len, hash)
        max_len=max(max_len,right+1-left)
        return max_len

        

        