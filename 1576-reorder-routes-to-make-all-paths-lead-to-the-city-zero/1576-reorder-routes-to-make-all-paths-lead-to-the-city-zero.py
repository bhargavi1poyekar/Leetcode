class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        roads = set()

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            roads.add((a, b))
        
        seen = {0}
        self.reroute = 0

        def dfs(city):
            for nghbr in graph[city]:
                if nghbr not in seen:
                    if (city, nghbr) in roads:
                        self.reroute += 1
                    seen.add(nghbr)
                    dfs(nghbr)
        
        dfs(0)
        return self.reroute