class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:

        inc_stack=[] # keep an monotonic increasing stack
        allowed_skips=len(nums)-k # number of val, we are allowed to skip

        for i in range(len(nums)): 
            while inc_stack and allowed_skips and inc_stack[-1]>nums[i]: # while curr num is smaller
                inc_stack.pop() # skip it and dec allowed skips
                allowed_skips-=1
            
            inc_stack.append(nums[i]) # append new number
        
        return inc_stack[:k] # return only the required array