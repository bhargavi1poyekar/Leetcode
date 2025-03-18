class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        word1_count = Counter(word1)
        word2_count = Counter(word2)

        word1_keys = set(word1_count.keys())
        word2_keys = set(word2_count.keys())

        word1_vals = sorted(word1_count.values())
        word2_vals = sorted(word2_count.values())

        return word1_keys == word2_keys and word1_vals == word2_vals
