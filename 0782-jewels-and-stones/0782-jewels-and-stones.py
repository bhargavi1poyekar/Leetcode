class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        stones_count=collections.Counter(stones)
        jewel_count=0
        for j in jewels:
            jewel_count+=stones_count[j]
        
        return jewel_count