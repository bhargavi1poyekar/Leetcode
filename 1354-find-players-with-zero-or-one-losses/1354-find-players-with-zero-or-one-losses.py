class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

       
        loses=collections.Counter()
        
        
        for i in range(len(matches)):
            loses[matches[i][0]]+=0
            loses[matches[i][1]]+=1
        
        
        notlost=[]
        lostone=[]
        for i in loses:
            if loses[i]==0:
                notlost.append(i)
            elif loses[i]==1:
                lostone.append(i)
    
        return [sorted(notlost),sorted(lostone)]
        
        