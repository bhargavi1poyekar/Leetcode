class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        Understand:

        Given -> arr of integers nums. 
        return leftmost pivot index. 

        pivot index => sum of all nums strictly to left = sum of alll nums strictly to right. 

        if no elements in left/ right -> left_sum/right_sum = 0

        if no such index, return -1

        Match: Prefix Sum

        Plan:
        we keep on adding leftsum. 
        and at beginning -> we calculate total_sum. 

        So right_sum = total - left - curr_element. 

        then check condition. if true, return index. 

        else, add currelement to leftSum. 
        '''

        left_sum = 0
        total_sum = sum(nums)

        for i, num in enumerate(nums):
            right_sum = total_sum - left_sum - num
            if left_sum == right_sum:
                return i
            left_sum += num
        
        return -1

        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''