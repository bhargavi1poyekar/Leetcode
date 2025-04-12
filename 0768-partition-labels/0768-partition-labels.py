class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_index = {}
        for i, ch in enumerate(s):
            last_index[ch] = i
        
        partition = []
        partition_start = 0
        partition_end = 0
        for i in range(len(s)):
            partition_end = max(partition_end, last_index[s[i]])

            if i == partition_end:
                partition.append(partition_end - partition_start + 1)
                partition_start = i + 1
        
        return partition


