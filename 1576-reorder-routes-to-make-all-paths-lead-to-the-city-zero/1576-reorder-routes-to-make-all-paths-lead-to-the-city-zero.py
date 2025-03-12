class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        self.reorder = 0
        graph = defaultdict(list)
        reversed_roads = set()

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            reversed_roads.add((a, b))
        
        # print(reversed_roads)
        # print(graph)
        seen = {0}

        def dfs(node):
            # print(node)
            for nghbr in graph[node]:
                if nghbr not in seen:
                    seen.add(nghbr)
                    if (node, nghbr) in reversed_roads:
                        # print(node, nghbr)
                        self.reorder += 1
                    dfs(nghbr)
        dfs(0)
        return self.reorder

