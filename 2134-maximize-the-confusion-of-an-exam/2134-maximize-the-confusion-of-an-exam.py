class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        char_freq={'T':0,'F':0} # Count of answers
        max_char=answerKey[0] # char with max freq
        left=0
        max_length=0

        for right in range(len(answerKey)):
            char_freq[answerKey[right]]+=1 # add char to window

            if char_freq[answerKey[right]]>char_freq[max_char]: # check if it should be new maxchar
                max_char=answerKey[right]
            
            if (right-left+1)-char_freq[max_char]>k: # if non max char are greater than k
                char_freq[answerKey[left]]-=1 # remove left
                left+=1
            
            max_length=max(max_length,right-left+1) # update max
        
        return max_length





