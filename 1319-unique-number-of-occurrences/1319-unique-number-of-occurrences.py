class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        freq_map = Counter(arr)

        count_freq = {}

        for key in freq_map:
            if freq_map[key] not in count_freq:
                count_freq[freq_map[key]] = 1
            else:
                count_freq[freq_map[key]] += 1

        
        for key in count_freq:
            if count_freq[key]!=1:
                return False
        
        return True
