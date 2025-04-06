class Solution:
    def convertToBase7(self, num: int) -> str:
        
        def base_7(num):
            conversion = []
            while num:
                conversion.append(str(num % 7))
                num = num // 7
            return conversion

        if num == 0:
            return '0'
        
        if num > 0:
            converted = base_7(num)
            return ''.join(converted[::-1])
        
        if num < 0:
            converted = base_7(abs(num))
            converted.append('-')
            return ''.join(converted[::-1])
        
