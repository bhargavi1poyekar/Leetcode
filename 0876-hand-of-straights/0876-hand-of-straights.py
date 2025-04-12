class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        hash_cards = Counter(hand)

        while hash_cards:
            start = min(hash_cards)

            for i in range(start, start + groupSize):
                if i not in hash_cards:
                    return False
                
                hash_cards[i] -= 1
                if hash_cards[i] == 0:
                    del hash_cards[i]
        
        return True
