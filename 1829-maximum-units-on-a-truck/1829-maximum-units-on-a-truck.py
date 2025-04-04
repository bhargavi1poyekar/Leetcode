class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes = sorted(boxTypes, reverse = True, key = lambda x:x[1])
        
        max_units = 0
        box = 0
        while truckSize > 0 and box < len(boxTypes):
            num_box = min(boxTypes[box][0], truckSize)
            max_units += num_box * boxTypes[box][1]
            truckSize -= num_box         
            box += 1
    
        return max_units