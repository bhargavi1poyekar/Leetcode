class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)

        for fromn, ton in edges:
            graph[ton].append(fromn)
        
        def dfs(node, seen):
            for nghbr in graph[node]:
                if nghbr not in seen:
                    seen.add(nghbr)
                    dfs(nghbr, seen)
            
            return seen

        ancestors = [sorted(dfs(node, set())) for node in range(n)]
        return ancestors
