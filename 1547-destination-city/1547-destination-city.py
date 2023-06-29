class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        src=collections.Counter()
        for i in paths:
            src[i[0]]+=1
            src[i[1]]+=0
        
        for i in src:
            if src[i]==0:
                return i