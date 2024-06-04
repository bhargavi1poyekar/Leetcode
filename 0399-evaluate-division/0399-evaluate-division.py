class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(start, end, ratio, seen):
            # no info on this node
            if start in graph:
                if start==end:
                    return ratio
                for nghbr in graph[start]:
                    if nghbr not in seen: 
                        seen.add(nghbr)
                        result=dfs(nghbr,end,ratio*graph[start][nghbr],seen)
                        if result!=-1:
                            return result
            return -1
        
        graph = defaultdict(dict)
        for i in range(len(equations)):
            numerator, denominator = equations[i]
            val = values[i]
            graph[numerator][denominator] = val
            graph[denominator][numerator] = 1 / val
        
        ans = []
        for numerator, denominator in queries:
            ans.append(dfs(numerator, denominator,1, {numerator}))
        
        return ans