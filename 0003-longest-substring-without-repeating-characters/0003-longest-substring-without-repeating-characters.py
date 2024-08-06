class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left =  0
        longest_length = 0
        hash_index = {}

        for right in range(len(s)):
            if s[right] in hash_index:
                left = max(left, hash_index[s[right]])
            
            longest_length = max(longest_length, right-left+1) 
            hash_index[s[right]] = right + 1 
        
        return longest_length

        # max_length = 0
        # left = 0
        # hash = {}
        # for right in range(len(s)):

        #     if s[right] in hash and hash[s[right]]>=left:
        #         left = max(left, hash[s[right]])
            
        #     hash[s[right]] = right+1
        #     max_length = max(max_length, right-left+1)

        # return max_length
            
