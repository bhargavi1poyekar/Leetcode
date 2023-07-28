class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:

        def digSum(num):
            dig_sum=0
            while num:
                dig_sum+=num%10
                num=num//10
            return dig_sum
        
        base=1
        add_int=0

        while digSum(n+add_int)>target:
            base*=10
            add_int=base-(n%base)
        
        return add_int
