class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        '''
        Understand:

        Given pattern and string.

        each letter -> maps to unique word in s
        unique word -> maps to exactly one letter. 

        no one to many, many to one. 

        Match: Hash to map the letters and word to each other.

        Plan:
        if num words != num_letters -> then return False

        s_map and p_map. 

        Now while traversing s and p. 
        check if s[i] mapped to p[i] and p[i] mapped to s[i]. 
        if not, return false. 

        if both dont exist in hash yet, add the mapping. 

        at end, if already not returned false, then return True.  
        '''

        # Implementation
        s = s.split(' ')
        s_map = defaultdict()
        p_map = defaultdict()

        # S and pattern length doest match -> mapping wont match
        if len(s) != len(pattern):
            return False
        
        for i in range(len(s)):
            # If both are not already map, we map them
            if s[i] not in s_map and pattern[i] not in p_map:
                s_map[s[i]] = pattern[i]
                p_map[pattern[i]] = s[i]
            
            # if one of them is mapped -> and mapped to some other character
            elif s[i] in s_map and s_map[s[i]] != pattern[i] or pattern[i] in p_map and p_map[pattern[i]] != s[i]:
                return False
        
        return True