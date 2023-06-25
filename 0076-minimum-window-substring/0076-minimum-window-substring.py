class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t)>len(s):return ""

        t_char=collections.Counter(t)
        unique=len(t_char)

        win_char=collections.Counter()
        match=0

        min_length=float('inf')
        min_right=0
        min_left=0

        left=0

        for right in range(len(s)):
            
            win_char[s[right]]+=1

            if t_char[s[right]]==win_char[s[right]]:
                match+=1
            
            

            while(unique==match):
                if right-left+1<min_length:
                    min_length=right-left+1
                    min_right=right
                    min_left=left

                if t_char[s[left]]==win_char[s[left]]:
                    match-=1
                
                win_char[s[left]]-=1
                left+=1
        
        return s[min_left:min_right+1] if min_length!=float('inf') else ""


