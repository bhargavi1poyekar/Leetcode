class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        max_char=s[0]
        left=0

        max_len=0

        freq=Counter()

        for right in range(len(s)):
            freq[s[right]]+=1

            if freq[s[right]]>=freq[max_char]:
                max_char=s[right]
            
            current_len=right-left+1

            if current_len-freq[max_char]>k:
                freq[s[left]]-=1
                left+=1
            
            max_len=max(max_len,right-left+1)

        return max_len
