class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        num_flowers = len(bloomDay)
        if m*k > num_flowers: return -1
        
        def check(days):
            curr_flowers = 0
            bouquet = 0
            i = 0

            while i < num_flowers:
                while i < num_flowers and bloomDay[i] <= days:
                    curr_flowers += 1
                    i += 1
                    if curr_flowers == k:
                        bouquet += 1
                        curr_flowers = 0
                if i < num_flowers and bloomDay[i] > days:
                    curr_flowers = 0
                # if bouquet > m: return True
                i += 1
            return bouquet >= m


        left = min(bloomDay)
        right = max(bloomDay)

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left