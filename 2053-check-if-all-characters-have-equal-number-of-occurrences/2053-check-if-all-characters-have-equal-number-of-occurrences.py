class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        # hash=collections.Counter()
        # for i in s:
        #     hash[i]+=1
        
        # exp=len(s)//len(hash)
        
        # for i in hash:
        #     if hash[i]!=exp:
        #         return False
        # return True
        
        return len(set(Counter(s).values())) == 1