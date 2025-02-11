class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def dfs(start, end, ratio, seen):
            if start == end:
                return ratio
            for nghbr in graph[start]:
                if nghbr not in seen:
                    seen.add(nghbr)
                    result = dfs(nghbr, end, ratio * graph[start][nghbr], seen)
                    if result != -1:
                        return result
            return -1

        graph = defaultdict(dict)

        for i in range(len(equations)):
            num, denom = equations[i]
            val = values[i]

            graph[num][denom] = val
            graph[denom][num] = 1 / val

        
        query_ans = []

        for num, denom in queries:
            if num in graph and denom in graph:
                query_ans.append(dfs(num, denom, 1, {num}))
            else:
                query_ans.append(-1)

        return query_ans
