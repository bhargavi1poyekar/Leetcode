class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs=sorted(costs)
        count=0
        # for i in costs:
        #     if coins>=i:
        #         count+=1
        #         coins-=i
        #     else:
        #         break

        # return count
        i=0
        while coins and i<len(costs):
            if coins>=costs[i]:
                count+=1
                coins-=costs[i]
            i+=1
        return count
