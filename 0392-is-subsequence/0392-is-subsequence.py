class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) > len(t):
            return False
        
        s_ptr = 0
        t_ptr = 0

        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            t_ptr += 1
        
        if s_ptr == len(s):
            return True
        
        return False