class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:

        stack=[]
        ans=[0 for i in range(len(heights))]
        for ht in range(len(heights)-1,-1,-1):
            count=0
            while stack and stack[-1]<heights[ht]:
                # print(stack)
                count+=1
                stack.pop()

            if stack:
                ans[ht]=count+1
            else:
                ans[ht]=count
            stack.append(heights[ht])
        
        return ans
            

