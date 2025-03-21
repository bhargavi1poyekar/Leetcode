class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        
        price.sort()

        def check(tastiness):
            count = 1
            last = price[0]
            for i in range(1, len(price)):
                if price[i] - last >= tastiness:
                    count += 1
                    last = price[i]
            
            return count >= k

        left = 0
        right = price[-1] - price[0]

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right
