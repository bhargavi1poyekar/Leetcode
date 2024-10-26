class Solution:
    def isHappy(self, n: int) -> bool:
        

        def square_sum(num):
            ans = 0
            while num:
                quot = num % 10
                ans += quot ** 2
                num = num // 10
            
            return ans

        cycle_check = set()
        num = n
        while num != 1:
            if num in cycle_check:
                return False
            else:
                cycle_check.add(num)
                num = square_sum(num)
                

        return True
    