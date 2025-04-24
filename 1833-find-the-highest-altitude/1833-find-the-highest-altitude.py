class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        '''
        Understand:

        road trip -> n + 1 points. at diff altitudes. 
        starts at point 0 -> altitude equal = 0

        given gain -> length n. net gain in altitude between i and i + 1

        Return highest altitude of point.  

        Match: Prefix Sum 

        Plan:
        Since gain can be negative -> 
        we keep on adding gain, and update max altitude. 
        '''

        max_alt = 0
        curr_alt = 0

        for net in gain:
            curr_alt += net
            max_alt = max(curr_alt, max_alt)

        return max_alt

        '''
        Time Complexity: O(N)
        Space COmplexitY: O(N)
        '''

        