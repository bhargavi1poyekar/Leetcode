class Solution:
    def partitionString(self, s: str) -> int:

        # lastseen=[-1]*26
        # count=1
        # sub_start=0

        # for i in range(len(s)):
        #     if lastseen[ord(s[i])-ord('a')]>=sub_start:
        #         count+=1
        #         sub_start=i
        #     lastseen[ord(s[i])-ord('a')]=i
        
        # return count

        lastseen={}
        count=1
        sub_start=0

        for i in range(len(s)):
            # print(lastseen, s[i], count, sub_start)
            if s[i] in lastseen and lastseen[s[i]]>=sub_start:
                count+=1
                sub_start=i
            lastseen[s[i]]=i
        return count

