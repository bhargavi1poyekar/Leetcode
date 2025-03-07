class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        curr_alt = 0
        max_alt = 0

        for inc in gain:
            curr_alt += inc
            max_alt = max(max_alt, curr_alt)
        
        return max_alt