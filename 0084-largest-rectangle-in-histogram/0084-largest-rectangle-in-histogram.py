class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack=[-1]
        max_area=0

        for right in range(len(heights)+1):

            while stack[-1]!=-1 and (right==len(heights) or heights[stack[-1]]>heights[right]):
                ht=heights[stack.pop()]
                w=right-stack[-1]-1
                max_area=max(max_area,ht*w)

            stack.append(right)
        
        return max_area

        


        

            
       
        




