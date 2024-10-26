class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        match_count = 0
        left = 0

        s1_hash = [0 for i in range(26)]
        s2_hash = [0 for i in range(26)]

        for i in range(len(s1)):
            s1_hash[ord(s1[i]) - ord('a')] += 1
            s2_hash[ord(s2[i]) - ord('a')] += 1
        
        match_count = 0

        for i in range(26):
            if s1_hash[i] == s2_hash[i]:
                match_count += 1
            
        for right in range(len(s1), len(s2)):
            if match_count == 26:
                return True

            right_idx = ord(s2[right]) - ord('a')
            s2_hash[right_idx] += 1
            
            if s2_hash[right_idx] == s1_hash[right_idx]:
                match_count += 1
            elif s2_hash[right_idx] - 1 == s1_hash[right_idx]:
                match_count -= 1
            
            left_idx = ord(s2[left]) - ord('a')
            s2_hash[left_idx] -= 1

            if s2_hash[left_idx] == s1_hash[left_idx]:
                match_count += 1
            elif s2_hash[left_idx] + 1 == s1_hash[left_idx]:
                match_count -= 1
            
            left += 1
        
        return match_count == 26
            

            
            
