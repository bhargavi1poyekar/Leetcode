class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        nums = sorted(zip(nums2, nums1), reverse = True)
        max_score = 0
        prefix = 0
        min_heap = []

        print(nums)

        for num2, num1 in nums:
            prefix += num1
            heapq.heappush(min_heap, num1)

            if len(min_heap) > k:
                prefix -= heapq.heappop(min_heap)
            
            if len(min_heap) == k:
                max_score = max(max_score, prefix*num2)
        
        return max_score