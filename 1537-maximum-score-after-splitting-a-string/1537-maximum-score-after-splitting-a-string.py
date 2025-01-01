class Solution:
    def maxScore(self, s: str) -> int:
        
        count_0 = 0
        count_1 = 0
        for i in range(len(s)):
            if s[i] == '0':
                count_0 += 1
            elif s[i] == '1':
                count_1 += 1
        
        # print(count_0, count_1)
        
        left_count_0 = 0
        left_count_1 = 0
        max_score = 0

        for right in range(len(s)-1):
            
            if s[right] == '0':
                left_count_0 += 1
            elif s[right] == '1':
                left_count_1 += 1

            curr_score = left_count_0 + (count_1 - left_count_1)
            max_score = max(curr_score, max_score) 
        
        return max_score



