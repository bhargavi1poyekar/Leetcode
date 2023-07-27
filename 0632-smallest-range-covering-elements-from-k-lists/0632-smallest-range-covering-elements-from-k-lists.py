class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        n=len(nums)
        elements=[0 for i in range(n)]
        min_heap=[(num[0],index) for index,num in enumerate(nums)]
        heapq.heapify(min_heap)
        curr_max=max(pair[0] for pair in min_heap)
        curr_min=min_heap[0][0]

        smallest_range=[curr_min,curr_max]

        if curr_min==curr_max:
            return smallest_range
        
        while True:
            _,index=heapq.heappop(min_heap)
            elements[index]+=1

            if elements[index]==len(nums[index]):
                return smallest_range
            
            if nums[index][elements[index]]>=curr_max:
                curr_max=nums[index][elements[index]]
            
            heapq.heappush(min_heap,(nums[index][elements[index]],index))
            curr_min=min_heap[0][0]

            if curr_max-curr_min<smallest_range[1]-smallest_range[0]:
                smallest_range=[curr_min,curr_max]
            
            if curr_min==curr_max:
                return smallest_range
