class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        min_heap=[]

        for i in range(candidates):
            min_heap.append((costs[i],0))
        
        for i in range(max(candidates,len(costs) - candidates),len(costs)):
            min_heap.append((costs[i],1))
        
        nextHead,nextTail=candidates,len(costs)-candidates-1
        heapq.heapify(min_heap)
        
        total_cost=0
        for _ in range(k):
            # print(min_heap)

            cost,half=heapq.heappop(min_heap)
            total_cost+=cost
            
            if nextHead<=nextTail:

                if half==0:
                    heapq.heappush(min_heap,(costs[nextHead],0))
                    nextHead+=1
                else:
                    heapq.heappush(min_heap,(costs[nextTail],1))
                    nextTail-=1
        
        return total_cost
        