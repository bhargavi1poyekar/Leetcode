class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for letter in ransom_count:
            if ransom_count[letter] > magazine_count[letter]:
                return False

        return True 