class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(dict)
        for i in range(len(equations)):
            num, denom = equations[i]
            graph[num][denom] = values[i]
            graph[denom][num] = 1/values[i]
        
        # print(graph)
        
        def dfs(num, denom, ratio, seen):
            if num == denom:
                return ratio
            
            for nghbr in graph[num]:
                if nghbr not in seen:
                    seen.add(nghbr)
                    result = dfs(nghbr, denom, ratio*graph[num][nghbr], seen)
                    if result != -1:
                        return result
            return -1
        
        query_ans = [] 
        for query in queries:
            num, denom = query
            if num not in graph or denom not in graph:
                query_ans.append(-1)
            else:
                query_ans.append(dfs(num, denom, 1, {num}))

        return query_ans 