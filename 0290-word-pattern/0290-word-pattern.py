class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        
        s_list=s.split(' ')
        if len(pattern)!=len(s_list):
            return False
        
        pattern_map={}
        s_map={}

        for i in range(len(pattern)):
            if pattern[i] not in pattern_map and s_list[i] not in s_map:
                pattern_map[pattern[i]]=s_list[i]
                s_map[s_list[i]]=pattern[i]

            elif  pattern_map.get(pattern[i])!=s_list[i] or s_map.get(s_list[i])!=pattern[i]:
                return False
            
        return True
