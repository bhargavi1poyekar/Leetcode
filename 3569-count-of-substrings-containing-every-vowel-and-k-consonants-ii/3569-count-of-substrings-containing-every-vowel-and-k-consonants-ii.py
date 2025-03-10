class Solution:
    def _isVowel(self, c: str) -> bool:
        return c in ["a", "e", "i", "o", "u"]

    def countOfSubstrings(self, word: str, k: int) -> int:

        def _isVowel(c):
            return c in ["a", "e", "i", "o", "u"]

        def atLeastK(word, k):
            num_valid_substrings = 0
            left = 0
            
            vowel_count = Counter()
            consonant_count = 0

            # start sliding window
            for right in range(len(word)):
                # insert new letter
                new_letter = word[right]

                # update counts
                if _isVowel(new_letter):
                    vowel_count[new_letter] += 1
                else:
                    consonant_count += 1

                # shrink window while we have a valid substring
                while len(vowel_count) == 5 and consonant_count >= k:
                    num_valid_substrings += len(word) - right
                    start_letter = word[left]
                    if _isVowel(start_letter):
                        vowel_count[start_letter] -= 1
                        if vowel_count[start_letter] == 0:
                            vowel_count.pop(start_letter)
                    else:
                        consonant_count -= 1
                    left += 1

                # end += 1

            return num_valid_substrings

        return atLeastK(word, k) - atLeastK(word, k + 1)
        ''' because atleast k contains
        exactly k, exactly k+1, k+2 and so on
        atleast k+1 contains:
        exactly k+1, k+2, k+3 and so on. 
        SO to find exactly k -> atleast(k) - atleast(k+1)
        '''