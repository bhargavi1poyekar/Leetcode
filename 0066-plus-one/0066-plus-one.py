class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        op = 0
        for d in digits:
            op = op*10 + d
        
        op += 1
        op = str(op)
        return [int(i) for i in op]