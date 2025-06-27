class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_count = Counter(nums)

        min_heap = []
        for num in nums_count:
            heapq.heappush(min_heap, (nums_count[num], num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for count, num in min_heap]
