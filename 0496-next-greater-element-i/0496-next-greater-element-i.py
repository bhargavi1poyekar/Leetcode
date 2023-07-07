class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Hash map to store next greater element of nums2
        next_greater={}
        stack=[] 

        for num in nums2:
            while stack and stack[-1]<num: # loop till new element is greater than top
                next_greater[stack.pop()]=num # for tops, curr element will be next greater
            
            stack.append(num) # add curr in stack
        
        while stack: # removing remaining elements who don't have next greater element
            next_greater[stack.pop()]=-1
        
        answer=[]
        for num in nums1: # now just check nums1 and get the answer array
            answer.append(next_greater[num])
        
        return answer

         


            