class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        stack=[-1]
        subsum=0
        for right in range(len(nums)+1):

            while stack[-1]!=-1 and (right==len(nums) or nums[stack[-1]]>=nums[right]):

                target=stack.pop()
                left=stack[-1]
                numsub=(target-left)*(right-target)
                subsum-=numsub*nums[target]
            
            stack.append(right)
        
        stack.clear()
        stack=[-1]

        for right in range(len(nums)+1):

            while stack[-1]!=-1 and (right==len(nums) or nums[stack[-1]]<=nums[right]):

                target=stack.pop()
                left=stack[-1]
                numsub=(target-left)*(right-target)
                subsum+=numsub*nums[target]
            
            stack.append(right)
        
        return subsum
        




