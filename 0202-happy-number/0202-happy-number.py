class Solution:
    def isHappy(self, n: int) -> bool:

        '''
        Understand:

        Given: n

        Todo:

        check if n is happy.
        conditions to be happy:
        any pos int n -> replace by sum of squares of its digit. 
        repeat this until 
        either n == 1 or loop in cycle -> which doesnt have 1. 

        if ends in n == 1 -> happy

        Return : true if happy, false if not.  

        cases: 
            if n == 0: return False. 
            if n -> single digit number -> return false. 

        Match:

        to check the cycle -> if the current number -> has been seen before -> we can use hash data structure. 

        if not, it will end in n==1. 

        Plan:

        fun sum_of_square_of_digits():
            first it will find digit by digit, and add its square to sum. 
            return the sum. 
        
        seen = set  -> any seen number is added to it. 
        while n != 1:
            if n in seen:
                return False -> cycle detected. 
            seen.add(n)
            n = sum_of_square_of_digits(n)
        
        return True
        '''

        def sum_of_square_of_digits(n):
            sum_square = 0

            while n:
                digit = n % 10
                n = n // 10
                sum_square += digit ** 2
            
            return sum_square
        
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum_of_square_of_digits(n)

        return True        




        