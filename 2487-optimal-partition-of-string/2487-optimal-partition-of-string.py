class Solution:
    def partitionString(self, s: str) -> int:

        lastseen=[-1]*26
        count=1
        sub_start=0

        for i in range(len(s)):
            if lastseen[ord(s[i])-ord('a')]>=sub_start:
                count+=1
                sub_start=i
            lastseen[ord(s[i])-ord('a')]=i
        
        return count