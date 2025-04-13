class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        '''
        Understand:

        Given -> 2 strings. s and t
        return if s subseq of t

        Match: 2 pointers. 1 for each string. 
        Plan:

        first of all, for s to be subseq, len(s) <= len(t)

        then, we have pointers at start of both strings. 
        if s[i] == t[i] :
            then move s ptr forward. 
        otherwise move t_ptr anyway. 

        continue this till we reach end of s or t. 
        if sptr reached end of s -> then s is sub seq of t. 
        '''

        # Implementation:

        if len(s) > len(t):
            return False
        
        s_ptr = 0
        t_ptr = 0

        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            t_ptr += 1
        
        return s_ptr == len(s)

        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''