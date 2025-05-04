class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        seen = Counter()
        pairs = 0

        for i, j in dominoes:
            if i != j:
                pairs += seen[(i, j)]
                pairs += seen[(j, i)]
            else:
                pairs += seen[(i, j)]

            seen[(i, j)] += 1
        
        return pairs

