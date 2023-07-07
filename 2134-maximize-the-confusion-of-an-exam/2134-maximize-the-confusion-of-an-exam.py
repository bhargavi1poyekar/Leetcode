class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        char_freq={'T':0,'F':0}
        max_char=answerKey[0]
        left=0
        max_length=0

        for right in range(len(answerKey)):
            char_freq[answerKey[right]]+=1

            if char_freq[answerKey[right]]>char_freq[max_char]:
                max_char=answerKey[right]
            
            if (right-left+1)-char_freq[max_char]>k:
                char_freq[answerKey[left]]-=1
                left+=1
            
            max_length=max(max_length,right-left+1)
        
        return max_length





