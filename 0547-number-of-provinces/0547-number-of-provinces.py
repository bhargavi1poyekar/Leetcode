class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(i, len(isConnected)):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        num_province = 0

        def dfs(node):
            for nghbr in graph[node]:
                if nghbr not in seen:
                    seen.add(nghbr)
                    dfs(nghbr)

        seen = set()
        for node in graph:
            if node not in seen:
                seen.add(node)
                num_province += 1
                dfs(node)
        
        return num_province