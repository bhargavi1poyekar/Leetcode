class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node):
            for child in graph[node]:
                if child not in seen:
                    seen.add(child) 
                    dfs(child)

        seen = {0}
        for node in restricted:
            seen.add(node)

        dfs(0)
        return len(seen) - len(restricted)
