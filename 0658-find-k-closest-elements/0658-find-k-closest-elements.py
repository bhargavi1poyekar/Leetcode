class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        max_heap = []

        for num in arr:
            diff = abs(num - x)
            heapq.heappush(max_heap, (-diff, -num))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return sorted([-close[1] for close in max_heap])
