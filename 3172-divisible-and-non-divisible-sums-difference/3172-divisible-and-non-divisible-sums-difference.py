class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        sum_num1 = 0
        sum_num2 = 0

        for num in range(1, n+1):
            if num % m != 0:
                sum_num1 += num
            else:
                sum_num2 += num
        
        return sum_num1 - sum_num2