class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        def binary_search(target):
            left = 0
            right = len(potions)

            while left < right:
                mid = (left + right) // 2
                if potions[mid] >= target:
                    right = mid
                else:
                    left = mid + 1

            return left

        potions.sort()
        ans = []
        potion_len = len(potions)

        for i in range(len(spells)):
            index = binary_search(success/spells[i])
            ans.append(potion_len - index)

        return ans 

