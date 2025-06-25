class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        combinations = []
        def backtrack(i, arr):
            if len(arr) == k:
                combinations.append(arr[:])
                return 
            
            for j in range(i+1, n+1):
                arr.append(j)
                backtrack(j, arr)
                arr.pop()
        
        backtrack(0, [])
        return combinations