class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:

        times=sorted(zip(growTime,plantTime), reverse=True)
       
        curr_time=0
        max_time=0

        for i in range(len(times)):
            curr_time+=times[i][1]
            max_time=max(max_time,curr_time+times[i][0])
        
        return(max_time)
