class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        '''
        Understand:

        Given -> nums and k
        h -> valid if all values  >  h are identical.
        h -> doesnt need to be in array. 

        Operation:
        1. Select h -> valid for curr values in nums
        2. For each index i, where nums[i] > h -> set nums[i] = h

        By doing this operation -> we need to make all values = k in min operations.

        Brute Force:

        Get hash -> distinct values.

        if k > min(value) -> not possible. 

        do this, till only 1 distinct value. 
        find max -> set h = second max -> and then convert all occ of max to h. 

        # Note: -> there is a trick to the question:
        if k is less tha min value -> then it is not possinle to vonvert to k. 
        But if k is present in the arr -> then we just need distinct_val - k operation, that is we convert all the numbers greater than k to k. Step by step. 

        So inshort it is just asking us how many distinct elements are greater than k.     
        '''

        # Approach 1
        hash_counter = Counter(nums)

        distinct_vals = len(hash_counter)

        if k > min(hash_counter):
            return -1
        
        if k in hash_counter:
            return distinct_vals - 1
        return distinct_vals

        # Approach 2
        count = 0
        
        for num in hash_counter:
            if num > k:
                count += 1
        
        return count
        

        
