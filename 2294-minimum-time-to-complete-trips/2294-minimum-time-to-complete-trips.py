class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def check(total_time):
            trips = 0
            for bustime in time:
                trips += total_time//bustime
            
            return trips >= totalTrips

        left = 1
        right = max(time) * totalTrips

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left