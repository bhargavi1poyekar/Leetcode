class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left=0
        maxChar=s[0]
        counter=collections.Counter()
        max_length=0

        for right in range(len(s)):

            # print(left,maxChar,counter, max_length,right)
            counter[s[right]]+=1
            if counter[s[right]]>=counter[maxChar]:
                maxChar=s[right]
            curr_len=right-left+1
            if (curr_len-counter[maxChar]>k):
                counter[s[left]]-=1
                left+=1
                curr_len=right-left+1
            
            max_length=max(max_length,curr_len)

        return max_length



