import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        # total_stones = sum(piles)
        piles = [-pile for pile in piles]
        heapq.heapify(piles)

        for _ in range(k):
            max_stones = heapq.heappop(piles)
            half = floor(max_stones // 2)
            heapq.heappush(piles, half)
        
        return -sum(piles)
        


