class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        min_heap = []
        min_heap.append((nums1[0]+nums2[0], 0, 0))

        min_sums = []
        seen = {(0, 0)}
        while k:
            _, i, j = heapq.heappop(min_heap)
            min_sums.append([nums1[i], nums2[j]])
            k -= 1

            if (i+1) < len(nums1) and (i+1, j) not in seen:
                sum = nums1[i+1] + nums2[j]
                heapq.heappush(min_heap, (sum, i+1, j))
            
            if (j+1) < len(nums2) and (i, j+1) not in seen:
                sum = nums1[i] + nums2[j+1]
                heapq.heappush(min_heap, (sum, i, j+1))
        
        return min_sums
                

