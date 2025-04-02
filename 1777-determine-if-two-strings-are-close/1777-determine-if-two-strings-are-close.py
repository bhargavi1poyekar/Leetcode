class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        word1_count = Counter(word1)
        word2_count = Counter(word2)

        word1_val = sorted(word1_count.values())
        word2_val = sorted(word2_count.values())

        word1_key = word1_count.keys()
        word2_key = word2_count.keys()

        return word1_key == word2_key and word1_val == word2_val

