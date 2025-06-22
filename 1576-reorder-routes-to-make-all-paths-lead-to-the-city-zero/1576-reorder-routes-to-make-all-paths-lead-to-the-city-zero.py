class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        roads = set()

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            roads.add((a, b))
        
        self.reorder = 0
        def dfs(node):
            for nghbr in graph[node]:
                if nghbr not in seen:
                    if (node, nghbr) in roads:
                        self.reorder += 1
                    seen.add(nghbr)
                    dfs(nghbr)

        seen = {0}
        dfs(0)

        return self.reorder 

