class Solution:
    def findLucky(self, arr: List[int]) -> int:

        lucky=[]
        count=collections.Counter(arr)
        # print(count)
        for i in count:
            if count[i]==i:
                lucky.append(i)

        return max(lucky) if len(lucky)!=0 else -1
