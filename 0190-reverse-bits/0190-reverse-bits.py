class Solution:
    def reverseBits(self, n: int) -> int:
        
        reverse = 0
        index = 31 # leftmost bit

        while n:
            digit = n & 1 # get 1 or 0 by & with 1
            reverse += digit << index # shift to that position. 
            n >>= 1 # Shift to next bit. 
            index -= 1 # next position. 
        
        return reverse
