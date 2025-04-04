class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Given: string s and k
        Choose any char of string and replace to any other uppercase english char. 
        Atmost k times. 

        empty string -> return 0
        s -> only Uppercase?

        Match: longest substring -> sliding window. 
        hash -> for freq counting -> to decide which character to replace with which char

        Plan:
        1. Have a freq counter of the chars encounterd so far. 
        2. Keep track of the max Char so far. 
        3. Start sliding window from first char, and keep adding new chars. 
        4. While adding new chars to sliding window -> inc freq in freq counter, and check if it has become max_char so far. -> update max_char accordingly/ 
        5. Now we check if curr len - freq of max char is > k -> because -> we want to replace the random chars with max char. so we check if the chars who are not max char > k, if yes, then we decrement the sliding window from left, and dec freq of left char. 
        6. After adjusting sliding window. Update max length of substring. 
        '''

        # Implementation

        if not s:
            return 0

        left = 0
        max_char = s[0]
        hash_freq = Counter()
        max_length = 0

        for right in range(len(s)):
            hash_freq[s[right]] += 1

            if hash_freq[s[right]] >= hash_freq[max_char]:
                max_char = s[right]
            
            curr_len = right - left + 1
            if curr_len - hash_freq[max_char] > k:
                hash_freq[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length

        '''
        Review:
        eg: ABAB, k = 2
        right = 3
        left = 0
        max_char = B
        hash_freq = Counter(A: 2, B: 2)
        max_length = 4
        curr_len = 4

        Evaluate:

        Time Complexity: O(n)
        Space Complexity: O(n) -> freq counter.
        '''