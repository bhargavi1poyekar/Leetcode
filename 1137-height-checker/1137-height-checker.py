class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        expected = sorted(heights)

        diff_indices = 0

        for i in range(len(expected)):
            if heights[i] != expected[i]:
                diff_indices += 1
        
        return diff_indices
        