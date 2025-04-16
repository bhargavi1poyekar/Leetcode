class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        '''
        Understand:

        Given: nums and k

        in 1 operation -> pick 2 numbers -> whose sum == k and remove them. 

        Return max operations possible. 

        Match: Sort and 2 pointers. 

        Plan
        Sort the array. -> have 2 pointers -> left and right

        if left + right num == k:
            numop += 1
        elif > k:
            right -= 1
        else:
            left += 1
        '''

        nums.sort()

        left = 0
        right = len(nums)-1

        num_op = 0

        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                num_op += 1
                left += 1
                right -= 1
            elif total > k:
                right -= 1
            else:
                left += 1
            
        return num_op

        '''
        Time Complexity : O nlogn  -> for sorting. 
        Space ComplexitY: O(n) -> for sorting. 
        '''
        