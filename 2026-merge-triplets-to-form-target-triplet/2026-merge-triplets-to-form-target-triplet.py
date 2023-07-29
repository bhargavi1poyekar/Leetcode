class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        valid_trip=[0]*3
        for t in triplets:
            # print(t,target)
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                continue
            
            for i in range(3):
                if t[i]==target[i]:
                    valid_trip[i]=t[i]

           
        return valid_trip==target


