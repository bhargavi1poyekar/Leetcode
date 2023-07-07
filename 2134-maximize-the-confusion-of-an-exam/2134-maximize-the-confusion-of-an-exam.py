class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        s=answerKey
        maxChar=s[0]
        charFreq=collections.Counter()
        left=0

        max_length=0

        for right in range(len(s)):
            charFreq[s[right]]+=1

            if charFreq[s[right]]>=charFreq[maxChar]:
                maxChar=s[right]
            
            current_len=right-left+1

            if(current_len-charFreq[maxChar]>k):
                charFreq[s[left]]-=1
                left+=1
            
            max_length=max(max_length,right-left+1)

        return max_length