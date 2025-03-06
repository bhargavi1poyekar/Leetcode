class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s_list = s.split(' ')
        
        if len(s_list) != len(pattern):
            return False
        
        s_map = defaultdict()
        pattern_map = defaultdict()

        # print(pattern_list)

        for i in range(len(s_list)):
            if s_list[i] not in s_map and pattern[i] not in pattern_map:
                s_map[s_list[i]] = pattern[i]
                pattern_map[pattern[i]] = s_list[i]
            
            elif s_map.get(s_list[i]) != pattern[i] or pattern_map.get(pattern[i]) != s_list[i]:
                return False
        
        return True