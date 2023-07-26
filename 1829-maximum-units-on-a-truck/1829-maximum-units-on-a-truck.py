class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        heap=[]

        for num_box, num_unit in boxTypes:
            heapq.heappush(heap,(-num_unit,num_box))
        
        total_unit=0

        while heap and truckSize:
            max_unit,num_box=heapq.heappop(heap)
            num_box_fit=min(truckSize,num_box)
            total_unit+=num_box_fit*(-max_unit)
            truckSize-=num_box_fit
        
        return total_unit
