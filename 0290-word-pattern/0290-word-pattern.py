class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        pattern_map = defaultdict()
        s_map = defaultdict()

        if len(s) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in pattern_map and s[i] not in s_map:
                pattern_map[pattern[i]] = s[i]
                s_map[s[i]] = pattern[i]
            
            elif pattern_map.get(pattern[i]) != s[i] or s_map.get(s[i]) != pattern[i]:
                return False
        
        return True