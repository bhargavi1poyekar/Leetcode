import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        '''
        Understand:

        Given -> 2 0-indexed int arrays nums1 and nums2 of length n.
        pos int k

        choose subseq of num1 of len k. 

        and for the same indices chosen -> select min val of nums2. 
        sum the nums1 chosen element * min nums2. 

        return max possible score. 

        Match: select min nums2, max possible score -> we can use heaps. 

        Plan:
        we want min of nums2. -> we can sort nums1 and nums2 based on nums2 in descending order. 

        then we can traverse over this, and keep prefix sum of nums1. 
        at every point we get min nums2 as we move forward. when we reach k -> we do the multiplication with prefix. 

        Now we need to exclude the nums1. so for this, we can add nums in min heap, and after we have k elements in heap, we can take out the min nums1. subtract it from prefix as well. 
        '''

        nums = sorted(zip(nums2, nums1), reverse = True)

        prefix_sum = 0
        min_heap = []
        max_score = float('-inf')

        for num2, num1 in nums:
            prefix_sum += num1
            heapq.heappush(min_heap, num1)

            if len(min_heap) == k:
                max_score = max(max_score, prefix_sum * num2)
                prefix_sum -= heapq.heappop(min_heap)
            
        return max_score

        '''
        Time Complexity: O(n log n) for sorting. 
        Space Complexity: O(k)
        '''