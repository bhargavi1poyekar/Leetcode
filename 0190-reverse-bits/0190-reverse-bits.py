class Solution:
    def reverseBits(self, n: int) -> int:
        
        reverse = 0
        index = 31

        while n:
            right_most_digit = n & 1
            reverse += right_most_digit << index
            n >>= 1
            index -= 1
        
        return reverse