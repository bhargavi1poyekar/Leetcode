class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        roads = set()

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            roads.add((u, v))
        
        def dfs(node):
            ans = 0
            for nghbr in graph[node]:
                if nghbr not in seen:
                    if (node, nghbr) in roads:
                        ans += 1
                    seen.add(nghbr)
                    ans += dfs(nghbr)
            
            return ans
        
        seen = {0}
        ans = dfs(0)
        return ans

