class Solution:
    def hammingWeight(self, n: int) -> int:
        set_bits = 0
        mask = 1

        # n & mask -> what this does is  -> at every digit -> it tries to & with 1 and if if gives 0 -> then it is not set. (every other bit will anyway result into 0 because we are & them with 0, only the current digit that we are checking is & with 1 -> so if 0 -> not set, if 1 -> set)

        # then mask is left shifted to move to next digit.
        for _ in range(32):
            if (n & mask) != 0:
                set_bits += 1
            n >>= 1
        return set_bits