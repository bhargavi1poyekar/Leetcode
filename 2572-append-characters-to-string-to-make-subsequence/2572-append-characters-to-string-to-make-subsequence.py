class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        j=0
        for i in range(len(s)):
            if j<len(t) and s[i]==t[j]:
                j+=1
        
        return 0 if j==len(t) else len(t)-j

            
        
