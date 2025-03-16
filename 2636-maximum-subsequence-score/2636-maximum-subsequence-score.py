class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        max_score = 0
        prefix_sum = 0
        min_heap = [] 

        group = sorted(zip(nums1, nums2), key = itemgetter(1), reverse = True)

        for num1, num2 in group:
            prefix_sum += num1
            heapq.heappush(min_heap, num1)
            
            if len(min_heap) == k:
                max_score = max(max_score, prefix_sum * num2)
                prefix_sum -= heapq.heappop(min_heap) # remove the min num1 from heap
        
        return max_score
            
