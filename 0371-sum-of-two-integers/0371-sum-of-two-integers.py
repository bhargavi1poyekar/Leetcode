class Solution:
    def getSum(self, a: int, b: int) -> int:
        '''
        Case 1: Same Signs (Addition)

        We care about sign of a -> because in addition -> we get the sign of bigger absolute value. 
        And adding or subtracting depends on if both positive/negative or one of them positive negative. 

        Example: a = 5, b = 3 (both positive)

        x, y = abs(5), abs(3) → x = 5, y = 3

        a * b = 15 > 0 → Use addition logic:

        Result: 8 * sign = 8 * 1 = 8

        Negative Example: a = -5, b = -3

        Same steps as above, but sign = -1 → Result: 8 * -1 = -8

        Case 2: Opposite Signs (Subtraction)
        Example: a = 5, b = -3

        x, y = abs(5), abs(-3) → x = 5, y = 3

        a * b = -15 < 0 → Use subtraction logic:

        Result: 2 * sign = 2 * 1 = 2 (5 - 3 = 2)

        Negative Example: a = -5, b = 3

        Same steps, but sign = -1 → Result: 2 * -1 = -2 (-5 + 3 = -2)
        '''
        x, y = abs(a), abs(b)
        # ensure x >= y
        if x < y:
            return self.getSum(b, a)  
            
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            # sum of two positive integers
            while y:
                x, y = x ^ y, (x & y) << 1
        else:
            # difference of two positive integers
            while y:
                x, y = x ^ y, ((~x) & y) << 1
        
        return x * sign