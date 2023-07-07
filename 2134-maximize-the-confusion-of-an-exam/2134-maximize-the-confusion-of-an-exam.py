class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        s=answerKey
        maxAns=answerKey[0]
        ansFreq=collections.Counter()
        left=0

        max_length=0

        for right in range(len(answerKey)):
            ansFreq[answerKey[right]]+=1

            if ansFreq[answerKey[right]]>=ansFreq[maxAns]:
                maxAns=answerKey[right]
            
            current_len=right-left+1

            if(current_len-ansFreq[maxAns]>k):
                ansFreq[answerKey[left]]-=1
                left+=1
            
            max_length=max(max_length,right-left+1)

        return max_length