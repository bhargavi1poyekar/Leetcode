class Solution:
    def hammingWeight(self, n: int) -> int:
        
        mask = 1
        num_set = 0
        while n:
            if n & mask:
                num_set += 1
            n >>= 1

        return num_set
