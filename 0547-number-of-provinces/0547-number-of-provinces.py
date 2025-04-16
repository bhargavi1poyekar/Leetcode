class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
        Understand -> n cities
        Some are connected, some are not

        Transitive Connection. 

        Province -> connceted cities. 

        Given: n * n matrix -> isConnected -> i j = 1 if i and j are connected. 

        else 0

        Return total provinces. 

        Match: Do Graph DFS traversal. Everytime new dfs -> increase num provinces. 

        Plan:
        First create graph of neighbors based on the given matrix. 

        Then do dfs, and maintain seen set to store nodes already seen. 

        Iterate over the cities, and if not in seen: we start dfs with that city. Go to its neighbors, add them into seen, and do this recursively. 
        '''

        graph = defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(i, len(isConnected)):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
            
        seen = set()

        def dfs(node):
            for nghbr in graph[node]:
                if nghbr not in seen:
                    seen.add(nghbr)
                    dfs(nghbr)
        
        num_province = 0
        for city in range(len(isConnected)):
            if city not in seen:
                num_province += 1
                seen.add(city)
                dfs(city)
        
        return num_province

        '''
        Time Complexity: O(n)
        Space Complexity: O(n) -> seen
        '''

        