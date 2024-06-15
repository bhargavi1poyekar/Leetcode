class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        num_proj=len(profits)
        projects=list(zip(capital,profits))
        projects.sort() # Sorts by capital
        # print(projects)

        max_heap=[]

        unv_ptr=0

        for i in range(k):
            while unv_ptr<num_proj and projects[unv_ptr][0]<=w:
                heappush(max_heap,-projects[unv_ptr][1])# Put profit in heap 
                unv_ptr+=1
            
            if max_heap:
                w+=-heappop(max_heap)
        
        return w