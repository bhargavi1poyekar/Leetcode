class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        arr_count=collections.Counter(arr)
        count={}
        for i in arr_count:
            if arr_count[i] in count:
                return False
            count[arr_count[i]]=i

        return True


