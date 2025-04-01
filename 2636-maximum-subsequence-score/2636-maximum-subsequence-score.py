import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        '''
        U:
        2 arrays -> nums1 and nums2 -> len n
        k 

        to do: 
        subsequence of indices of nums1 of len k
        for these indices:
            scores -> (sum of selected elements from num1) * min(nums2 [indices])
        
        to return: max possible score

        Understanding with example

        nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
        0, 1, 2 -> 7 * 1 -> 7
        1, 2, 3 -> 8 * 1 -> 8
        0, 1, 3 -> 6 * 1 -> 6
        0, 2, 3 -> 6 * 2 -> 12

        max -> 12

        Questions:
        if empty arr -> score 0?
        if always nums1 len == nums len ?
        can any case have k > n? if yes what to return. 

        Match:

        Since according to this question, we might need max nums, and min nums2, so -> heap good option. 

        Plan:
        Since order of the sequence doesnt matter exactly. we just need to have same indices fr both nums1 and nums2.

        1. Sort our nums2 -> in ascending order.
        2. And nums1 -> should be arranged acc to nums2 indices. 

        (nums1, nums2)
        zip = [, , , ] # sorted zip. 
            [(2, 4), (3, 3), (1, 2), (3, 1)]

        Now lets have a heap. 

        lets iterate over this zip. 
        and then min_nums2 = nums2

        min_heap.append(nums1)

        if len(min_heap) == k:
            max = max(max, sum(min_heap) * nums2)
            min_heap.pop
        '''

        # Implementation

        sorted_zip = sorted(zip(nums2, nums1), reverse = True)     
        max_score = float('-inf')
        min_heap = []
        prefix_sum = 0
        for num2, num1 in sorted_zip:
            heapq.heappush(min_heap, num1)
            prefix_sum += num1

            if len(min_heap) == k:
                score = prefix_sum * num2
                max_score = max(max_score, score)
                prefix_sum -= heapq.heappop(min_heap)
        
        return max_score

        '''
        sorted_zip = [(2, 4), (3, 3), (1, 2), (3, 1)]
        min_heap = [2, 3, 3]
        max_score = 12
        k = 3
        num1 = 3, num2 = 1
        score = 8

        '''
