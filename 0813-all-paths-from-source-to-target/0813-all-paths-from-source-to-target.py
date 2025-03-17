class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        ans = []
        def backtrack(node, curr):
            if node == n - 1:
                ans.append(curr[:])
                return
            
            for nghbr in graph[node]:
                curr.append(nghbr)
                backtrack(nghbr, curr)
                curr.pop()
        
        backtrack(0, [0])
        return ans
                
