class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        if len(cards)<2:
            return -1

        left=0
        min_cards=float('inf')
        hash_set=collections.Counter()
        for right in range(0,len(cards)):
                # print(hash_set,min_cards, cards[right])
                while(hash_set[cards[right]]>=1):
                    min_cards=min(min_cards,right-left+1)
                    hash_set[cards[left]]-=1
                    left+=1

                hash_set[cards[right]]+=1
            
                
        return min_cards if min_cards!=float('inf') else -1