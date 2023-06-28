class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        ispan=[0 for i in range(26)]

        for i in sentence:
            ispan[ord(i)-ord('a')]+=1
        
        for i in range(26):
            if ispan[i]<1:
                return False
            
        return True