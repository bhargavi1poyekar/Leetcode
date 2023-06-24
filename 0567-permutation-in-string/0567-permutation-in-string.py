from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1)>len(s2):return False
    
        s1_count=[0 for i in range(26)]
        s2_count=[0 for i in range(26)]

        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')]+=1
            s2_count[ord(s2[i])-ord('a')]+=1

        match_count=0

        for i in range(26):
            if s1_count[i]==s2_count[i]:
                match_count+=1
        
        left=0
        for right in range(len(s1),len(s2)):
            if match_count==26:
                return True

            idx=ord(s2[right])-ord('a')
            s2_count[idx]+=1
            if s2_count[idx]==s1_count[idx]:
                match_count+=1
            elif s2_count[idx]-1==s1_count[idx]:
                match_count-=1
            
            idx=ord(s2[left])-ord('a')
            s2_count[idx]-=1

            if s2_count[idx]==s1_count[idx]:
                match_count+=1
            elif s2_count[idx]+1==s1_count[idx]:
                match_count-=1
            
            left+=1
        
        return match_count==26

            
            
