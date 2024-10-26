class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        t_count = [0 for i in range(26)]

        for i in range(len(s)):
            t_count[ord(t[i]) - ord('a')] += 1
            t_count[ord(s[i]) - ord('a')] -= 1
        
        for i in range(26):
            if t_count[i] != 0:
                return False
        
        return True
        