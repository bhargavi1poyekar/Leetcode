class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        '''
        Understand:

        Given: nums -> find subarr with largest prod and return prod. 
        
        the integers will be negative ? yes
        will there be 0 ? yes

        Match: If not negative intergers -> we could have used greedy approach like Kadane's algorithm. Where if the subarray prod is lesser than curr element. then it wont exactly contribute, and hence we drop it. 

        But here because of Negative integers and prod. -> 2 negative integers give a positive product. So here we can do is get max and min. because if we get any 2 non negative integers, then previous negative product can be saved. 

        '''
        if not nums:
            return -1

        max_so_far = nums[0]
        min_so_far = nums[0]

        max_prod = nums[0]

        for i in range(1, len(nums)):
            temp_max = max(nums[i], max_so_far * nums[i], min_so_far * nums[i])
            min_so_far = min(nums[i], max_so_far * nums[i], min_so_far * nums[i])
            max_so_far = temp_max
            max_prod = max(max_prod, max_so_far)
        
        return max_prod

        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''

