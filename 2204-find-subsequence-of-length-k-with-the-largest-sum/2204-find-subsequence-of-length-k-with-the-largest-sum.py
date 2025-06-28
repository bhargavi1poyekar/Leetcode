class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        min_heap = []

        for idx, val in enumerate(nums):
            heapq.heappush(min_heap, (val, idx))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        min_heap.sort(key=lambda x: x[1])
        return [val for val, _ in min_heap]