class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def backtrack(curr, i):
            # print(curr,i)
            if i == len(graph)-1:
                ans.append(list(curr))
                return
            
            for node in graph[i]:
                curr.append(node)
                backtrack(curr, node)
                curr.pop()
        
        ans = []
        backtrack([0], 0)
        return ans