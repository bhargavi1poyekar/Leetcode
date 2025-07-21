class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        min_diff = float('inf')

        pairs = []

        for i in range(1, len(arr)):
            a = arr[i-1]
            b = arr[i]

            curr_diff = b - a

            if curr_diff < min_diff:
                min_diff = curr_diff
                pairs = [[a, b]]
            elif curr_diff == min_diff:
                pairs.append([a, b])
        
        return pairs
