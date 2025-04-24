class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Understand:

        Given an int arr -> nums -> return all triplets
        nums[i], nums[j], nums[k]

        their sums = 0

        Solution must not contain duplicate triplets. 


        Match: We can sort and make use of two pointer 2 sum solution in this. 

        Like, convert 3 sum into 2 sum. 

        Plan:

        for two sum we required -> sorted array -> so we need to sort it. 
        Then convert 3 sum to 2 sum. 

        in two sum, we were given target, and we needed to find sum of 2 elements == target. 

        here, we want sum of all 2 to be 0
        num1 + num2 + num3 = 0
        num1 + num2 = -num3

        So for every element -> we can send the remaining array as list, and -element as target as input to 2 sum function. 
        '''

        # Implementation

        def twoSum(nums, target):

            left = 0
            right = len(nums) - 1
            triplets = []

            while left < right:
                if nums[left] + nums[right] == target:
                    # If we get the sum to be 0, add it to solution
                    triplets.append([nums[left], nums[right], -target])
                    left += 1
                    right -= 1

                    # To check if we are not adding duplicate elements. 
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
            
            return triplets
        
        nums.sort() # for two sum. 
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                # if element is greater than 0, and arr is already sorted, so no future elements can sum to 0
                break
            elif i > 0 and nums[i] != nums[i-1]:
                ans.extend(twoSum(nums[i+1:], -nums[i]))
            elif i == 0: 
                ans.extend(twoSum(nums[i+1:], -nums[i]))
        
        return ans

        '''
        Time Complexity: O(nlogn) + O(n^2) -> O(n^2)
        Space Complexity: O(n)
        '''

