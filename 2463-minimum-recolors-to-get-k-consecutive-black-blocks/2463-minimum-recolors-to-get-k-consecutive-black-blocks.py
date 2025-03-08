class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        left = 0
        min_ops = float('inf')
        ops = 0

        for right in range(len(blocks)):
            if blocks[right] == 'W':
                ops += 1
            
            while right - left + 1 >= k:
                min_ops = min(ops, min_ops)
                if blocks[left] == 'W':
                    ops -= 1
                left += 1

        return min_ops
