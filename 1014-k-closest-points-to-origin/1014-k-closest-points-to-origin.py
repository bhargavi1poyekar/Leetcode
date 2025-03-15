class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def find_distance(point):
            return point[0]**2 + point[1]**2

        max_heap = []

        for point in points:
            distance = find_distance(point)
            heapq.heappush(max_heap, (-distance, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [pair[1] for pair in max_heap]
