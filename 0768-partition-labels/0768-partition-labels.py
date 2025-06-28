class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_index = defaultdict(int)

        for i, ch in enumerate(s):
            last_index[ch] = i
        
        start_p = 0
        max_p_end = 0
        partition_size = []

        for i, ch in enumerate(s):
            max_p_end = max(max_p_end, last_index[ch])
            if i == max_p_end:
                size = max_p_end - start_p + 1
                partition_size.append(size)
                start_p = i + 1
        
        return partition_size
            
            
