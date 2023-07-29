class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_occ=Counter()

        for i in range(len(s)):
            last_occ[s[i]]=i
        
        partition_size=[]
        curr_size=0
        curr_end=last_occ[s[0]]
        for i in range(len(s)):
            curr_end=max(curr_end,last_occ[s[i]])
            curr_size+=1
            if i==curr_end:
                partition_size.append(curr_size)
                curr_size=0
        
        return(partition_size)
