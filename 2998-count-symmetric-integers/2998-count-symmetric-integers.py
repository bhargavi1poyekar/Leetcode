class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0  # Initialize counter for special numbers
    
        for num in range(low, high + 1):  # Check each number in range
            
            # Case 1: Two-digit numbers with identical digits (11, 22, ... 99)
            if num < 100 and num % 11 == 0:
                res += 1
            
            # Case 2: Four-digit numbers where first half sum equals second half sum
            elif 1000 <= num < 10000:
                # Calculate sum of first two digits
                thousands = num // 1000
                hundreds = (num % 1000) // 100
                first_half_sum = thousands + hundreds
                
                # Calculate sum of last two digits
                tens = (num % 100) // 10
                units = num % 10
                second_half_sum = tens + units
                
                # Check if sums match
                if first_half_sum == second_half_sum:
                    res += 1
                
        return res
    