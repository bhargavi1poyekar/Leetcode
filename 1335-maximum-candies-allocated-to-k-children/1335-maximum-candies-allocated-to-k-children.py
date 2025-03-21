class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def check(each_c):
            num_children = 0
            for candy in candies:
                num_children += candy // each_c 

            return num_children >= k 

        left = 1
        right = sum(candies)//k

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right