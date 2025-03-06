class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        count = Counter(arr)

        counter_hash = {}

        for num in count:
            if count[num] in counter_hash:
                return False
            counter_hash[count[num]] = 1
        
        return True