class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_map=collections.Counter()
        t_map=collections.Counter()

        for i in range(len(s)):

            if s[i] not in s_map and t[i] not in t_map:
                s_map[s[i]]=t[i]
                t_map[t[i]]=s[i]
            
            elif s_map.get(s[i])!=t[i] or t_map.get(t[i])!=s[i]:
                return False
        
        return True
