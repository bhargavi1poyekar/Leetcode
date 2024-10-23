class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p)>len(s):return []
    
        p_count=[0 for i in range(26)]
        s_count=[0 for i in range(26)]

        for i in range(len(p)):
            p_count[ord(p[i])-ord('a')]+=1
            s_count[ord(s[i])-ord('a')]+=1

        match_count=0

        for i in range(26):
            if p_count[i]==s_count[i]:
                match_count+=1
        
        left=0
        anagram_idx = []
        for right in range(len(p),len(s)):
            if match_count==26:
                anagram_idx.append(left)

            idx=ord(s[right])-ord('a')
            s_count[idx]+=1
            if s_count[idx]==p_count[idx]:
                match_count+=1
            elif s_count[idx]-1==p_count[idx]:
                match_count-=1
            
            idx=ord(s[left])-ord('a')
            s_count[idx]-=1

            if s_count[idx]==p_count[idx]:
                match_count+=1
            elif s_count[idx]+1==p_count[idx]:
                match_count-=1
            
            left+=1

        if match_count==26:
            anagram_idx.append(left)
        
        return anagram_idx 
