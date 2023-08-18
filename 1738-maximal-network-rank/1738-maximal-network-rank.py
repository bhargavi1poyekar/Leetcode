class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        degree=Counter()
        graph=defaultdict(set)

        for a,b in roads:
            graph[a].add(b)
            graph[b].add(a)
        
        max_rank=0
        for i in range(n):
            for j in range(i+1,n):
                curr_rank=len(graph[i])+len(graph[j])
                if j in graph[i]:
                    curr_rank-=1
                
                max_rank=max(max_rank,curr_rank)
        
        return max_rank


