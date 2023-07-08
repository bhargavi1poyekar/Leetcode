class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:

        stack=[]
        seeCount=[0 for i in range(len(heights))]

        for ht in range(len(heights)-1,-1,-1):
            smallerPeople=0
            while stack and heights[stack[-1]]<heights[ht]:
                stack.pop()
                smallerPeople+=1
            
            if not stack:
                seeCount[ht]=smallerPeople
            else:
                seeCount[ht]=smallerPeople+1
            
            stack.append(ht)
        
        return seeCount