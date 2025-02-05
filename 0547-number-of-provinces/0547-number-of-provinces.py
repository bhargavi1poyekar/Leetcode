class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected)):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        def dfs(node):
            for nghbr in graph[node]:
                if nghbr not in seen:
                    seen.add(nghbr)
                    dfs(nghbr)
        
        seen = set()
        num_province = 0

        for i in range(len(isConnected)):
            if i not in seen:
                num_province += 1
                seen.add(i)
                dfs(i)
        
        return num_province
