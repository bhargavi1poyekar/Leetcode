class Solution:
    def longestPalindrome(self, s: str) -> int:

        s_counter=Counter(s)

        odd=0
        longest=0

        for v in s_counter.values():
            if v%2==0:
                longest+=v
            else:
                odd=1
                longest+=(v-1)
        
        return longest+odd