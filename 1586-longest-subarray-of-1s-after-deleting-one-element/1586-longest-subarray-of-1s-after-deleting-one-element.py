class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        Understand:

        given -> binary arr -> 0, 1 only
        delete 1 (only) element. 
        return size of longest non empty subarr -> only 1 in result arr. 

        Questions?
        if all are 0 -> we return 0
        if empty -> we return 0

        Match: subarr -> sliding window. 
        longest -> variable sliding window size.    

        so if we get one 0 -> as we cna delete only 1 -> we start sliding the window.

        Plan:
        start with 0, 0 window. 
        if 1, just expand window from right.
        if one 0 -> its fine -> since we can delete it.  
        if more than one 0 -> then we need to slide the window, contract from left. -> till 0 is within limit

        as we have to delete an element even if it is 1/0 -> we calculate length with right - left 

        and update max length at every iteration. 
        '''

        # Implement

        left = 0
        max_length = 0
        count_0 = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count_0 += 1
            
            while count_0 > 1:
                if nums[left] == 0:
                    count_0 -= 1
                left += 1

            max_length = max(max_length, right - left)
        
        return max_length

        '''
        Review:

        nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
        left = 5
        right = 8

        max_length = 5
        count_0 = 1

        Evaluate:

        Time Complexity : O(n) 
        Space Complexity : O(1)
        '''


