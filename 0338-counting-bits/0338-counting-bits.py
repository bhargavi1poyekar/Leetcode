class Solution:
    def countBits(self, n: int) -> List[int]:
        def pop_count(x: int) -> int:
            count = 0
            mask = 1
            while x:
                if (x & mask) != 0:  
                    count += 1
                x >>= 1
            return count
            
        ans = [0] * (n + 1)
        for x in range(n + 1):
            ans[x] = pop_count(x)
    
        return ans                