class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        Understand:

        given 2 strings s and t 
        isomorphic -> if chars in s -> replaced to get t. 

        mapping should be one to one. 
        char may map to itself. 

        Match: -> we match the mappings in hash. 

        Plan:
        if length of both strings not equal -> return False. 

        Now, while traversing both the strings at same time, we check if any of the curr char of both string is already mapped. if not mapped, then we map s[i] => t[i] and vice versa. 

        if mapped -> then check if mapped to same character, else, return false. 

        at end -> return true. 
        '''

        if len(s) != len(t):
            return False
        
        s_map = defaultdict()
        t_map = defaultdict()

        for i in range(len(s)):
            if s[i] not in s_map and t[i] not in t_map:
                s_map[s[i]] = t[i]
                t_map[t[i]] = s[i]
            elif s[i] in s_map and s_map[s[i]] != t[i] or t[i] in t_map and t_map[t[i]] != s[i]:
                return False
    

        return True

        '''
        Time complexity: O(N)
        Space Complexity: O(N)
        '''