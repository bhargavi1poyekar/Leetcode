class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t)>len(s):return "" # If t>s no substring

        t_freq=Counter(t)
        unique_t_char=len(t_freq)
        win_freq=Counter()

        left=0
        min_len=float('inf')
        min_left=0
        min_right=0

        match_count=0

        for right in range(len(s)):
            win_freq[s[right]]+=1

            if win_freq[s[right]]==t_freq[s[right]]:
                match_count+=1
            
            while match_count==unique_t_char:
                if right-left+1 <min_len:
                    min_len=right-left+1
                    min_left=left
                    min_right=right

                if win_freq[s[left]]==t_freq[s[left]]:
                    match_count-=1
                win_freq[s[left]]-=1
                left+=1
            
        return s[min_left:min_right+1] if min_len!=float('inf') else ""


       