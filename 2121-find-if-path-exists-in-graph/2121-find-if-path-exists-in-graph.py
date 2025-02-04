class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def dfs(node):
            for nghbr in graph[node]:
                if nghbr not in seen:
                    seen.add(nghbr)
                    dfs(nghbr)

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = {source}
        dfs(source)

        if destination in seen:
            return True
        return False
        
