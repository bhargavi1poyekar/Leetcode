class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack=[-1]
        max_area=0

        for right in range(len(heights)):

            while stack[-1]!=-1 and heights[stack[-1]]>=heights[right]:
                h=heights[stack.pop()]
                w=right-stack[-1]-1
                max_area=max(max_area,h*w)
            
            stack.append(right)
        
        while stack[-1]!=-1:
            h=heights[stack.pop()]
            w=len(heights)-stack[-1]-1
            max_area=max(max_area,h*w)
        
        return max_area
            
       
        




