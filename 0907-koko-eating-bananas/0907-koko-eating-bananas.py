class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            sum_time = 0
            for ban in piles:
                sum_time += ceil(ban/k)
            
            return sum_time <= h

        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left 
