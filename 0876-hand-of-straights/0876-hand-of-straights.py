class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize:
            return False
        
        hash_count = Counter(hand)

        heap = list(hash_count.keys())
        heapq.heapify(heap)

        while heap:
            first = heap[0]
            for i in range(first, first + groupSize):
                if i not in hash_count:
                    return False
                hash_count[i] -= 1
            
                if hash_count[i] == 0:
                    heapq.heappop(heap)
        
        return True