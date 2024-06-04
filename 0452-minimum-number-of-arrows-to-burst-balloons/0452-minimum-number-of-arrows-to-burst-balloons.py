class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        
        count=1
        end_ptr=points[0][1]
        for s,e in points:
            if s>end_ptr:
                end_ptr=e
                count+=1
        return count