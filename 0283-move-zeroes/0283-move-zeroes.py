class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        Understand:

        Given -> arr nums -> move all 0's to end. 
        Inplace. without making a copy of array. 

        Match: slow, fast pointer. 

        Plan:
        slow pointer at start.

        Inc fast pointer ahead -> till you find a non zero element. Assign it to slow pointer, and inc slow pointer. 

        Do this till fast reaches end of nums. 
        then for remaining 0's, just replace the remaing element after slow to 0.  

        '''

        slow = 0
        fast = 0

        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        while slow < len(nums):
            nums[slow] = 0
            slow += 1
        
        return nums

        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''

