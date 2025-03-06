class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_count=collections.Counter(word1)
        word2_count=collections.Counter(word2)

        print(word1_count)
        print(word2_count)

        word1_keys=set(word1_count.keys())
        word2_keys=set(word2_count.keys())

        print(word1_keys)
        print(word2_keys)

        word1_values=sorted(word1_count.values())
        word2_values=sorted(word2_count.values())

        print(word1_values)
        print(word2_values)

        return True if word1_keys==word2_keys and word1_values==word2_values else False