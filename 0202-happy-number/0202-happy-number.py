class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sum_square_of_digits(n):
            sum_square = 0

            while n:
                digit = n % 10
                n = n // 10
                sum_square += digit ** 2

            return sum_square

        hash_map = set()

        while n != 1:
            if n in hash_map:
                break
                
            hash_map.add(n)
            n = sum_square_of_digits(n)

        
        return n == 1
