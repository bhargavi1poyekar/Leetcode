class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        max_heap = []
        projs = sorted(zip(capital, profits))

        proj_idx = 0

        for i in range(k):
            while proj_idx < len(projs) and projs[proj_idx][0] <= w:
                heapq.heappush(max_heap, -projs[proj_idx][1])
                proj_idx += 1
            
            if max_heap:
                w -= heapq.heappop(max_heap)

        return w

