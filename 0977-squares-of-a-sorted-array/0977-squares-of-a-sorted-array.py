class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        '''
        2 pointers
        '''

        left = 0 
        right = len(nums)-1

        squares = [0]*len(nums)
        ptr = len(nums)-1

        while left <= right:
            if nums[left]**2 >= nums[right]**2:
                squares[ptr] = nums[left]**2
                left += 1
            else:
                squares[ptr] = nums[right]**2
                right -= 1
            ptr -= 1

        return squares