class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        answer=0
        stack=[-1]

        for right in range(len(nums)+1):
            while stack[-1]!=-1 and (right==len(nums) or nums[stack[-1]]>=nums[right]):
                target_min=stack.pop()
                num_sub=(target_min-stack[-1])*(right-target_min)
                answer-=num_sub*nums[target_min]
            stack.append(right)
        
        stack.clear()
        stack=[-1]

        for right in range(len(nums)+1):
            while stack[-1]!=-1 and (right==len(nums) or nums[stack[-1]]<=nums[right]):
                target_min=stack.pop()
                num_sub=(target_min-stack[-1])*(right-target_min)
                answer+=num_sub*nums[target_min]

            stack.append(right)

        return answer
        




