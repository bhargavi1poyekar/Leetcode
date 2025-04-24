class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Understand: 
        Given an int array nums
        return true of any value appears atleast twice. 

        And return false otherwise.

        Match -> set -> to keep track of element we have seen. 

        Plan: if element is already in set: return True. 
        else at end,return false
        '''

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False

        '''
        Time Complexity: O(N)
        Space COmplexity: O(N)
        '''        

        