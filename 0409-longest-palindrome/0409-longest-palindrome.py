class Solution:
    def longestPalindrome(self, s: str) -> int:

        hash_map = Counter(s)
        palindrome_length = 0
        odd_freq = False

        for char in hash_map:
            if hash_map[char] % 2 == 0:
                palindrome_length += hash_map[char]
            else:
                if not odd_freq:
                    palindrome_length += hash_map[char]
                    odd_freq = True
                else:
                    palindrome_length += hash_map[char] - 1

        return palindrome_length 
        