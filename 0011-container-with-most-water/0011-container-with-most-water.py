class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        start = 0
        end = len(height) - 1
        max_area = 0

        while start <= end:
            hght = min(height[start], height[end])
            width = end - start
            area = hght*width
            max_area = max(area, max_area)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area