class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

       
        # loses=collections.Counter()
        
        # for i in range(len(matches)):
        #     loses[matches[i][0]]+=0
        #     loses[matches[i][1]]+=1
        
        
        # notlost=[]
        # lostone=[]
        # for i in loses:
        #     if loses[i]==0:
        #         notlost.append(i)
        #     elif loses[i]==1:
        #         lostone.append(i)
    
        # return [sorted(notlost),sorted(lostone)]

        # Since players are in the range of 0,len(matches):

        loses=[-1 for i in range(100001)]

        for i in matches:
            if loses[i[0]-1]==-1:
                loses[i[0]-1]=0
            if loses[i[1]-1]==-1:
                loses[i[1]-1]=1
            else:loses[i[1]-1]+=1

        # print(loses)
        notlost=[]
        lostone=[]
       
        for i in range(len(loses)):
            if loses[i]==0:
                notlost.append(i+1)
            elif loses[i]==1:
                lostone.append(i+1)
        return [notlost,lostone]
        