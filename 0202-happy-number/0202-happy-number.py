class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sum_square(num):
            square = 0
            while num:
                digit = num % 10
                num = num // 10
                square += digit ** 2
            
            return square
        
        seen = set()
        num = n

        while num != 1:
            if num in seen:
                break
            else:
                seen.add(num)
                num = sum_square(num)
        
        if num == 1:
            return True
        else: return False