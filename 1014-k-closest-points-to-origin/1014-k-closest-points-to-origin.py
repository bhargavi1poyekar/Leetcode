class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def find_distance(x, y):
            return sqrt(x**2 + y**2)
        
        max_heap = []
        for x, y in points:
            distance = find_distance(x, y)
            heapq.heappush(max_heap, (-distance, x, y))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        closest = [[x, y] for _, x, y in max_heap]
        return closest
        