class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        Understand:

        height -> len n -> n lines

        return: max amt of water. 

        what if height is empty -> no lines -> max amt -> 0?

        Match: 
        2 pointer -> start from both ends, and then start decreasing the width as we move ahead. 

        Plan:

        amt of water = > area of the container
        area = width * height
        width - > right - left + 1 -> left is ptr from left, and right starts from end. 

        height => min(height[left], height[right])
        ''' 

        left = 0 
        right = len(height)-1
        max_area = 0
        while left < right:
            width = right - left
            hgt = min(height[left], height[right])
            area = width * hgt
            max_area = max(max_area, area)

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        
        return max_area