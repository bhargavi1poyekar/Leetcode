class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        players=set()
        loses=collections.Counter()
        
        for i in range(len(matches)):
            players.add(matches[i][0])
            players.add(matches[i][1])
            loses[matches[i][1]]+=1
        
        
        notlost=[]
        lostone=[]
        for i in players:
            if i not in loses:
                notlost.append(i)
            elif loses[i]==1:
                lostone.append(i)
    
        return [sorted(notlost),sorted(lostone)]
        
        