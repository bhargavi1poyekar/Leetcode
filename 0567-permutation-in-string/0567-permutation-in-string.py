class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        match_count = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                match_count += 1
        
        left = 0
        for right in range(len(s1), len(s2)):
            if match_count == 26:
                return True

            right_index = ord(s2[right]) - ord('a')
            s2_count[right_index] += 1

            if s1_count[right_index] == s2_count[right_index]:
                match_count += 1
            elif s1_count[right_index] == s2_count[right_index] - 1:
                match_count -= 1
            
            left_index = ord(s2[left]) - ord('a')
            s2_count[left_index] -= 1

            if s1_count[left_index] == s2_count[left_index]:
                match_count += 1
            elif s1_count[left_index] == s2_count[left_index] + 1:
                match_count -= 1
            
            left += 1
        
        return match_count == 26

            

            

            
        


