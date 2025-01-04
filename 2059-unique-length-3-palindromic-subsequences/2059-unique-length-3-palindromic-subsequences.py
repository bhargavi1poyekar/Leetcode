class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        '''
        For counting only the unique ones we can push in hashmap. 
        We have to find palindrome of only length 3. So start and end needs to be same. 
        and middle can be anything. 
        
        Approach 1:

        Let's we have 2 pointers -> If we mak them start from 0. 
        Then slow will be at beginning -> we can move fast till end till we find the same letter again. 
        if not found same letter we incr slow, and then change fast to slow + 1

        Now if we find same letter, then we have new pointer that starts from slow till fast and then with every character in between we create a string and put it in the hashset. 

        Once it reaches fast, we can again continue moving fast till end so that it checks if we get that letter again. If yes, then we need to keep that ptr continuing till the next same letter. 

        Once reached end. Move slow + 1, and then fast = slow + 1  

        But this is not optimal approach, since we pass the array too many times. 

        Approach 2: Optimized

        1. Compute the first and last index for each character. 
        2. Then for every letter (26), find the letters in between the first and las occ of that letter. if there is not first occ, then continue. 
        3. Put each letter in between in a hashset, and then calculate the length of the hashshet for the number of unique palindroms. 
        '''

        first = [-1] * 26
        last = [-1] * 26

        for i in range(len(s)):
            curr_letter = ord(s[i]) - ord('a')
            if first[curr_letter] == -1:
                first[curr_letter] = i
            
            last[curr_letter] = i
        
        unique_palindromes = 0

        for i in range(26):
            if first[i] == -1:
                continue

            in_betn = set()
            for i in range(first[i]+1, last[i]):
                in_betn.add(s[i])
            
            unique_palindromes += len(in_betn)

        return unique_palindromes
            






