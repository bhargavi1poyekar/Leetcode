class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        def binary_search(left, right, spell):
            while left < right:
                mid = (left + right) // 2
                if potions[mid]*spell >= success:
                    right = mid
                else:
                    left = mid + 1
            
            return left

        left = 0
        right = len(potions)

        potions.sort()
        total_spells = len(spells)
        pairs = [0] * total_spells

        for i in range(len(spells)):
            index = binary_search(left, right, spells[i])
            pairs[i] = right - index
        
        return pairs