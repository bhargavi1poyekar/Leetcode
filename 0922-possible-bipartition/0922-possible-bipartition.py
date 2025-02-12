class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, color):
            node_colors[node] = color
            for nghbr in graph[node]:
                if node_colors[nghbr] == node_colors[node]:return False
                if node_colors[nghbr] == -1:
                    if not dfs(nghbr, 1-color):
                        return False
            return True 

        node_colors = [-1] * (n+1)

        for i in range(1, n + 1):
            if node_colors[i] == -1:
                if not dfs(i, 0):
                    return False
        
        return True
            

