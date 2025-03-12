class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(dict)

        for i in range(len(equations)):
            num = equations[i][0]
            denom = equations[i][1]
            graph[num][denom] = values[i]
            graph[denom][num] = 1/values[i]


        def dfs(num, denom, ratio, seen):
            if num == denom: return ratio
            for nghbr in graph[num]:
                if nghbr not in seen:
                    seen.add(nghbr)
                    result = dfs(nghbr, denom, ratio*graph[num][nghbr], seen)
                    if result != -1:
                        return result
            
            return -1
        ans = []
        for query in queries:
            num = query[0]
            denom = query[1]
            if num in graph and denom in graph:
                ans.append(dfs(num, denom, 1, set()))
            else:
                ans.append(float(-1))
        
        return ans