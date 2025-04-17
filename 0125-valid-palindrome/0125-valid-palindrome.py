class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        '''
        Understand:

        Given -> palindrome -> converting all uppercase into lowercase and removing non alpha numeric chars -> reads same back and forward. 

        Match: 2 pointer. 

        Plan: First remove any non alphanumeric characters. Then have 2 pointers start and end. COmpare till the pointers are equal or if vals are not same return false. 

        '''

        s_list = []
        for ch in s:
            if ch.isalnum():
                s_list.append(ch.lower())
        
        # print(s_list)
        start = 0
        end = len(s_list) -1 

        while start <= end:
            if s_list[start] != s_list[end]:
                return False
            
            start += 1
            end -= 1
        
        return True

        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''