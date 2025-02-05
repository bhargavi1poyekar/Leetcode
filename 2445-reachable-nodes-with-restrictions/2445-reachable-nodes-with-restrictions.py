class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        graph = defaultdict(list)

        for u, v in edges:
            print(u, v)
            graph[u].append(v)
            graph[v].append(u)

        print(graph)
        
        def dfs(node):
            for child in graph[node]:
                # print(node, child)
                if child not in seen:
                    seen.add(child) 
                    dfs(child)

        seen = {0}
        for node in restricted:
            seen.add(node)

        dfs(0)
        # print(seen)
        return len(seen) - len(restricted)
