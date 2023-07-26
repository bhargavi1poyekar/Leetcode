class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts=Counter(arr)
        arr=sorted(counts.values(),reverse=True)

        while k:
            val=arr[-1]
            if val<=k:
                k-=val
                arr.pop()
            else:
                break
        
        return len(arr)