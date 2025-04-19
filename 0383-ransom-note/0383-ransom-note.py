class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        '''
        Understand:
        Given 2 strings -> ransomNote and magazine
        return True if ransomNote can be made using letters from magazine. 
        else False

        Each latter can be used once.

        Match: Hash -> to check count of letters. 

        Plan:
        for each letter in ransomNote the count should be <= magazine count of that letter. 

        if not, return False
        '''

        note_count = Counter(ransomNote)
        mag_count = Counter(magazine)

        for letter in note_count:
            if note_count[letter] > mag_count[letter]:
                return False

        return True        

        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''