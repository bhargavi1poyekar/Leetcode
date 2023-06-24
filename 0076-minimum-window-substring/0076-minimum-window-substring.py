class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_char=collections.Counter(t)
        unique_t=len(t_char)

        win_char=collections.Counter()
        
        left=0
        min_length=float('inf')
        min_right=0
        min_left=0

        match=0

        for right in range(len(s)):
            
            win_char[s[right]]+=1

            if win_char[s[right]]==t_char[s[right]]:
                match+=1
            
            while(match==unique_t):
                if min_length>right-left+1:
                    min_length=right-left+1
                    min_left=left
                    min_right=right

                if win_char[s[left]]==t_char[s[left]]:
                    match-=1

                win_char[s[left]]-=1
                left+=1

        return s[min_left:min_right+1] if min_length!=float('inf') else ""
            
            