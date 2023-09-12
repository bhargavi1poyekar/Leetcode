class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        cities=Counter()

        for src,dest in paths:
            cities[src]+=1
            cities[dest]+=0
        
        for city in cities:
            if cities[city]==0:
                return city
        

        