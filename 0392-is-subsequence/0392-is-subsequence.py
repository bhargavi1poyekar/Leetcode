class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) > len(t):
            return False

        s_ptr = len(s) - 1
        t_ptr = len(t) - 1

        while t_ptr > -1 and s_ptr > -1:
            if s[s_ptr] == t[t_ptr]:
                s_ptr -= 1
            t_ptr -= 1
        
        # print(s_ptr)
        if s_ptr < 0:
            return True

        return False

