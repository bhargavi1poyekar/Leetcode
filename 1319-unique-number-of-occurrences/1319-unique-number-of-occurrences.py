class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        arr_count=Counter(arr)

        unique=len(set(arr_count.values()))

        return unique==len(arr_count)
        