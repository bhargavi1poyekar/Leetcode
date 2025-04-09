class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        '''
        Understand:

        Given sorted arr and target val. 
        return index if target is found. 
        else return where it would be inserted. 

        Match:
        Binary Search - > insert position. 
        '''

        left = 0
        right = len(nums) 
        ''' 
        we dont take len(nums)-1 because if target not found, 
        we need to find insert position. 
        there is possibility, that it needs to be inserted at the end. 
        SO we require extra index. 
        '''

        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        return left

        '''
        Time Complexity : log n
        Space Complexity: O(1)
        '''

