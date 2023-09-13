class Solution:
    def customSortString(self, order: str, s: str) -> str:

        s_freq=Counter(s)

        ans=''
        for ch in order:
            if ch in s_freq:
                ans+=ch*s_freq[ch]
                del s_freq[ch]
        
        for i in s_freq:
            ans+=i*s_freq[i]
        
        return ans

        