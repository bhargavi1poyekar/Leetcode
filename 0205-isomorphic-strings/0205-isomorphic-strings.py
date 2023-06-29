class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # s_ind=[]
        # t_ind=[]

        # for i in s:
        #     s_ind.append(s.index(i))
        
        # for i in t:
        #     t_ind.append(t.index(i))
        

        # if s_ind==t_ind:
        #     return True
        # return False

        s_map={}
        t_map={}

        for i in range(len(s)):
            if s[i] not in s_map and t[i] not in t_map:
                s_map[s[i]]=t[i]
                t_map[t[i]]=s[i]
            
            elif s_map.get(s[i])!=t[i] or t_map.get(t[i])!=s[i]:
                return False
        
        return True
