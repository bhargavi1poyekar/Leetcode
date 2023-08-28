class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        # s=sorted(s)
        # t=sorted(t)

        # if s==t:
        #     return True
        # return False


        counter=[0 for i in range(26)]

        for i in range(len(s)):
            counter[ord(s[i])-ord('a')]+=1
            counter[ord(t[i])-ord('a')]-=1
        
        for count in counter:
            if count!=0:
                return False
        return True

