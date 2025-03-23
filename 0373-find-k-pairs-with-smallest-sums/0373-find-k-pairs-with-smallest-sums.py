class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        min_heap = [(nums1[0]+nums2[0], 0, 0)]
        smallest_sum_pair = []
        seen = {(0, 0)}

        while k > 0:
            _, i, j = heapq.heappop(min_heap)
            smallest_sum_pair.append([nums1[i], nums2[j]])

            if i+1 < len(nums1) and (i+1, j) not in seen:
                seen.add((i+1, j))
                heapq.heappush(min_heap, (nums1[i+1]+nums2[j], i+1, j))
            
            if j+1 < len(nums2) and (i, j+1) not in seen:
                seen.add((i, j+1))
                heapq.heappush(min_heap, (nums1[i]+nums2[j+1], i, j+1))
            
            k -= 1

        return smallest_sum_pair 
            



