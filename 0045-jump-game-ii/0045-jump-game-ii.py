class Solution:
    def jump(self, nums: List[int]) -> int:
        
        '''
        Understand:

        Given -> 0 indexed arr of integers. nums of length n. 
        Initially at nums[0]

        each element -> represents max length of forward jump from i. 

        return min jumps to reach nums[n-1]. 

        Match: Greedy approach. 

        Plan:
        initially we have left and right limits. -> set to 0. 

        Now, as we go ahead. we iterate from left till right, and get the max jump that is possible. 

        Then left = right. and right = max jump possible. 

        increament the number of jmp by 1. -> since it is considered that we jumped to max jump. 

        then again this is continued till we reach n-1. 
        '''

        left = 0
        right = 0
        n = len(nums)

        min_jumps = 0

        while right < n-1:
            max_jump = 0

            for i in range(left, right+1):
                max_jump = max(max_jump, i + nums[i])
            
            left = right
            right = max_jump
            min_jumps += 1
        
        return min_jumps

        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
            

 