class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand)%groupSize:
            return False

        card_count=Counter(hand)
        min_heap=list(card_count.keys())
        heapify(min_heap)

        while min_heap:
            min_card=min_heap[0]
            for i in range(min_card,min_card+groupSize):
                
                if i not in card_count:
                    return False
                card_count[i]-=1
                if card_count[i]==0:
                    if min_heap[0]!=i:
                        return False
                    heappop(min_heap)
        return True
