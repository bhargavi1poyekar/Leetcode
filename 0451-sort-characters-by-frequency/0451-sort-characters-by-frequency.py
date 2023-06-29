class Solution:
    def frequencySort(self, s: str) -> str:

        

        freq=collections.Counter(s)
        count=[[] for i in range(len(s)+1)]

        for i in freq:
            count[freq[i]].append(i)
            
        ans=[]
        for i in range(len(count)-1,0,-1):
            for c in count[i]:
                ans.append(c*i)

        return ''.join(ans)


