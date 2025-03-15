import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_freq = Counter(nums)
        min_heap = []
        for num in nums_freq:
            heapq.heappush(min_heap, (nums_freq[num], num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            
        return [count[1] for count in min_heap]

