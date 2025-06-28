class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary_search(spell_strength):

            left = 0
            right = len(potions)
            while left < right:
                mid = left + (right - left) // 2
                potion_strength = potions[mid]
                prod = potion_strength * spell_strength

                if prod >= success:
                    right = mid
                else:
                    left = mid + 1
            return left

        potions.sort()
        pairs = [0]*len(spells)
        m = len(potions)

        for i in range(len(spells)):
            index = binary_search(spells[i])
            pairs[i] = m - index
        
        return pairs

        