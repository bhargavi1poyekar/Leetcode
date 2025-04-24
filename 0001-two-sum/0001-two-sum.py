class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Understand: 

        Given int arr nums -> and target. 
        return indices of 2 nums -> add up to target. 

        exactly 1 solution. 
        not use same element twice. 

        Match: hash -> to keep track of prev elements 

        Plan:
        we add target-element in hash and its index. 

        everytime we check if curr element in target. if yes -> return indexes.
        '''

        hash_sum = {}

        for i, num in enumerate(nums):
            if num in hash_sum:
                return [hash_sum[num], i]
            else:
                hash_sum[target-num] = i

        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        
