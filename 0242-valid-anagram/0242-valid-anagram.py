class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Understand:

        Given s and t -> return True if t is anagram of s. 
        
        Anagram -> both have same characters -> with same count, but different order

        Brute Force -> sort and compare. 
        Optimized -> counter -> Match the hash of both strings. 

        '''    

        return Counter(s) == Counter(t)

        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
    