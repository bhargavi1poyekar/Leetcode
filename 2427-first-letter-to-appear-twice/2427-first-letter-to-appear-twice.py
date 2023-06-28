class Solution:
    def repeatedCharacter(self, s: str) -> str:

        hash={}
        for i in s:
            if i in hash:
                return i
            else:
                hash[i]=1