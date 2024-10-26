class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magazine_counter = Counter(magazine)
        ransom_counter = Counter(ransomNote)

        for ch in ransomNote:
            if magazine_counter[ch] < ransom_counter[ch]:
                return False
        
        return True