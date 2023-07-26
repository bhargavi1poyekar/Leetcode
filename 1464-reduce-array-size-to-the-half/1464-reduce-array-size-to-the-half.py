class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        half_arr=len(arr)//2
        freq=sorted(Counter(arr).values())
        # print(freq)
        ans=0
        while half_arr>0 and freq:
            
            half_arr-=freq[-1]
            freq.pop()
            ans+=1

        return ans

