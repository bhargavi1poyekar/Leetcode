class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_triplet = [0] * 3
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            for i in range(3):
                if t[i] == target[i]:
                    max_triplet[i] = t[i]
        
        return max_triplet == target
                    
