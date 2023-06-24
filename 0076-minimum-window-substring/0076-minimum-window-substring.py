class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t)>len(s):return ""
        

        t_count=collections.Counter(t)
        unique_char=len(t_count)
      
        win_count=collections.Counter()

        left=0  
        sub_char=0
        min_length=float('inf')
        min_left=0
        min_right=0
        
        for right in range(len(s)):
            win_count[s[right]]+=1

            if win_count[s[right]]==t_count[s[right]]:
                sub_char+=1
            
            while(left<=right and sub_char==unique_char):
                if right-left+1<min_length:
                    min_length=right-left+1
                    min_left=left
                    min_right=right
                
                if win_count[s[left]]==t_count[s[left]]:
                    sub_char-=1
                win_count[s[left]]-=1
                left+=1
        
        return '' if min_length==float('inf') else s[min_left:min_right+1]

