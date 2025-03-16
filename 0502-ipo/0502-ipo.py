class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        group = sorted(zip(capital, profits))
        index = 0
        max_heap = []

        for i in range(k):
            while index < len(group) and group[index][0] <= w:
                heapq.heappush(max_heap, -group[index][1])
                index += 1

            if max_heap:
                w -= heapq.heappop(max_heap)

        return w
