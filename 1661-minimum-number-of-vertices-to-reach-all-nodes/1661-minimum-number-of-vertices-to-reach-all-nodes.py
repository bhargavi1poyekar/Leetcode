class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        indegree = Counter()

        for u, v in edges:
            indegree[v] += 1
        
        node_set = []

        for node in range(n):
            if not indegree[node]:
                node_set.append(node)
        
        return node_set
         
        