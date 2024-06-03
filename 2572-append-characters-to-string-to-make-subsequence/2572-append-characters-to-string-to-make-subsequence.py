class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        match_count = 0
        s_ptr = 0
        t_ptr = 0

        while s_ptr < len(s) and t_ptr < len(t):

            if s[s_ptr] == t[t_ptr]:
                match_count += 1
                t_ptr += 1
            
            s_ptr += 1
        
        return len(t) - match_count

