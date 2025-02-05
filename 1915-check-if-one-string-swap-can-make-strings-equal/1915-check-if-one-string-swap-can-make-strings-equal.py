class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        if len(s1) != len(s2):
            return False
        
        non_equal = 0
        s1_diff = set()
        s2_diff = set()

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                non_equal += 1
                s1_diff.add(s1[i])
                s2_diff.add(s2[i])
        
        if non_equal != 0 and non_equal != 2:
            return False
        
        return s1_diff == s2_diff
        


