class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        Understand:

        Given -> binary arr -> elements 0 or 1 and int k
        return max num of consecutive 1's in arr -> if you can flip at most k 0's

        Match: Variable Size sliding window. 

        Plan: 
        We keep count of how many 0 we encountered, and we can flip at most k 0's. 

        So if the count > k:
        then we remove element from left, till count > k. 

        And keep on updating max length of sliding window. 
        '''

        left = 0
        max_ones = 0
        count_0 = 0 

        for right in range(len(nums)):
            if nums[right] == 0:
                count_0 += 1
            
            while count_0 > k:
                if nums[left] == 0:
                    count_0 -= 1
                left += 1
            
            max_ones = max(max_ones, right - left + 1)
        
        return max_ones

        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''