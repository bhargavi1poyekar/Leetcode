import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        '''
        Given: nums and k
        Return kth largest element. 

        k be 0? no
        if nums empty -> return -1?

        will there be duplicates -> yes
        kth in sorted order -> not kth distinct element. 

        Match -> 1. Brute force -> sort the array -> return k - 1 th element
        2. Heap -> if top kth element

        Plan -> since we want largest element -> we can use min heap. 
        and just keep on adding num to heaps -> once we find len(heap) > k:
        we start popping. 

        At the end -> heap top -> kth largest element. 

        Because. we will remove all other elements lesser than k. So the elements in the heap -> highest k elements. top of the heap -> smallest -> min heap. so it would be kth largest. 
        '''

        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0]

        '''
        Time Complexity -> for each heappush -> log n, heappop -> log n
        At every num -> we are pushing -> and also might be popping.  and heap size limited to k. 
        so n log k. 

        Space -> O(k)
        
        '''