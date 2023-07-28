class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:

        minheap=nums
        heapify(minheap)

        for i in range(k):
            heappush(minheap,-heappop(minheap))
        
        return sum(minheap)
