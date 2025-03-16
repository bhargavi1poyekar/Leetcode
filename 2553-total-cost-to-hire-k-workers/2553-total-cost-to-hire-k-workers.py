class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        min_heap = []
        n = candidates

        for i in range(n):
            min_heap.append((costs[i], 0))
        
        for i in range(len(costs)-1, max(len(costs)-n-1, n-1), -1):
            min_heap.append((costs[i], 1))

        heapq.heapify(min_heap)

        left = n
        right = len(costs)-n-1
        total_cost = 0

        for _ in range(k):
            cost, half = heapq.heappop(min_heap)
            total_cost += cost

            if left <= right:
                if half == 0:
                    heapq.heappush(min_heap, (costs[left], 0))
                    left += 1
                else:
                    heapq.heappush(min_heap, (costs[right], 1))
                    right -= 1
        
        return total_cost

