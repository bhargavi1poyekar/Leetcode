class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        '''
        # Linear Complexity
        count_pos = 0
        count_neg = 0

        for num in nums:
            if num < 0:
                count_neg += 1
            elif num > 0:
                count_pos += 1
        
        return max(count_neg, count_pos)
        '''

        # Binary Search: log complexity. 

        # Search for 0: get index, from index find, num pos, and num neg 

        def lower_bound(nums):
            start, end = 0, len(nums) - 1
            index = len(nums)

            while start <= end:
                mid = (start + end) // 2
                if nums[mid] < 0:
                    start = mid + 1
                else:
                    end = mid - 1
                    index = mid

            return index
        
        def upper_bound(nums):
            start, end = 0, len(nums) - 1
            index = len(nums)

            while start <= end:
                mid = (start + end) // 2

                if nums[mid] <= 0:
                    start = mid + 1
                else:
                    end = mid - 1
                    index = mid

            return index

        positiveCount = len(nums) - upper_bound(nums)
        # All integers from the index 0 to index before the first zero index
        # will be negative.
        negativeCount = lower_bound(nums)

        return max(positiveCount, negativeCount)
            
