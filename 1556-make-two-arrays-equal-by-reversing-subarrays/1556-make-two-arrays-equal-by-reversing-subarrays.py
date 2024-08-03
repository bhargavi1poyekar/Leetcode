class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        target_dict = Counter(target)
        arr_dict = Counter(arr)

        return target_dict == arr_dict
