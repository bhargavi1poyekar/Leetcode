class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''
        Understand:

        Given -> int array -> nums consist of n elements. and int k. 

        Find -> continguous sub whose len is k. and has max avg val. 
        Return max avg. 

        Match: Sliding window -> fixed length

        Plan:

        First fill k elements in the windows. 
        keep curr sum. 

        Now one by one add one element and remove one element. Adjust the sum accordingly. 
        Update max sum. 

        At end take average. 
        '''

        # max_sum = float('-inf')
        curr_sum = 0

        for i in range(k):
            curr_sum += nums[i]
        
        max_sum = curr_sum
        left = 0

        for right in range(k, len(nums)):
            curr_sum += nums[right] - nums[left]
            max_sum = max(max_sum, curr_sum)
            left += 1

        # print(max_sum)
        return max_sum / k 

        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
