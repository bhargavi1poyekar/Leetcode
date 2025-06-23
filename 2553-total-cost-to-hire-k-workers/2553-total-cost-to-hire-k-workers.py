class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        min_heap = []

        for i in range(candidates):
            min_heap.append((costs[i], 0))
        
        for i in range(len(costs)-1, max(len(costs)-candidates-1, candidates-1), -1):
            min_heap.append((costs[i], 1))

        heapq.heapify(min_heap)

        first_idx = candidates
        second_idx = len(costs)-candidates-1

        total_cost = 0
        for i in range(k):
            cost, half = heapq.heappop(min_heap)
            total_cost += cost

            if first_idx <= second_idx:
                if half == 0:
                    heapq.heappush(min_heap, (costs[first_idx], 0))
                    first_idx += 1
                else:
                    heapq.heappush(min_heap, (costs[second_idx], 1))
                    second_idx -= 1
        
        return total_cost

