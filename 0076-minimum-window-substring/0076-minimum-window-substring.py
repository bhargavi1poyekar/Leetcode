class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t)>len(s):return "" # If t>s no substring

        t_char=collections.Counter(t) # Char freq for t
        unique=len(t_char) # unique characters in t

        win_char=collections.Counter() # Char freq for window
        match=0  # Match count of window and t

        min_length=float('inf') 
        min_right=0
        min_left=0

        left=0

        for right in range(len(s)):
            
            win_char[s[right]]+=1 # inc window count

            if t_char[s[right]]==win_char[s[right]]: # If window count of char matches t count of char
                match+=1

            while(unique==match): # If all unique char match
                if right-left+1<min_length: # Update min
                    min_length=right-left+1 
                    min_right=right
                    min_left=left

                if t_char[s[left]]==win_char[s[left]]: # If they match before removing, dec match 
                    match-=1
                
                win_char[s[left]]-=1 # dec wi freq
                left+=1 # Inc window length
        
        return s[min_left:min_right+1] if min_length!=float('inf') else "" 


