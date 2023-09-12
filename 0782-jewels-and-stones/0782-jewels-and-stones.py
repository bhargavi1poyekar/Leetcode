class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        stones_count=Counter(stones)
        
        count=0
        for stone in stones_count:
            if stone in jewels:
                count+=stones_count[stone]
        
        return count

        