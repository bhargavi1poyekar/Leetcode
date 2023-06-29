class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransom=collections.Counter(ransomNote)
        mag=collections.Counter(magazine)

        for i in ransom:
            
            if ransom[i]>mag[i]:
                return False
        return True