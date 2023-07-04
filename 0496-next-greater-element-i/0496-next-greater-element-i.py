class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack=[]
        hash_pair={}
        for i in range(len(nums2)):
            while stack and nums2[i]>stack[-1]:
                hash_pair[stack.pop()]=nums2[i]
            stack.append(nums2[i])

        while stack:
            hash_pair[stack.pop()]=-1
        

        ans=[]
        for i in nums1:
            if i in hash_pair:
                ans.append(hash_pair[i])
            else:
                ans.append(-1)
        
        return ans



            