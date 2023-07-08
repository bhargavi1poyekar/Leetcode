class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:

        inc_stack=[]
        allowed_skips=len(nums)-k

        for i in range(len(nums)):
            while inc_stack and allowed_skips and inc_stack[-1]>nums[i]:
                inc_stack.pop()
                allowed_skips-=1
            
            inc_stack.append(nums[i])
        
        return inc_stack[:k]