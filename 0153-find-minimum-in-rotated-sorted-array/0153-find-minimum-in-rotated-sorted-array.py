class Solution:
    def findMin(self, nums: List[int]) -> int:

        '''
        Understand:

        Given  -> rotated sorted array -> initially the array was sorted. But now we rotated it by some number k. 

        We need to find the minimum element -> min element -> means without rotation it was the first array. 

        Match: 1. Traverse and update min -> O(n) -> Brute Force Solution. 
        2. Binary Search. -> since it is a sorted array.

        Plan:

        initially this was a sorted array. 

        it will still be sorted, only at a certain index it would be -> nums[i] > nums[i+1] -> we dont know in which direction we need to take mid -> after comparison. 

        lets notice that -> nums[i] > nums[-1] (last index) -> if this is true -> we know that smaller element is to the right -> left -> mid + 1

        else:nums[i] < nums[-1] -> it can be to the left -> right = mid - 1

        [3, 4, 5, 1, 2] 

        we decrease our search space by half -> by comparing mid -> with the last element. 
        '''
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        
        return nums[left] 

        '''
        Time Complexity : O(log n)
        Space Complexity : O(1)
        '''