class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        '''
        Understand:

        Given an arr of real numbers -> values 
        equations = A, B
        A/B = val

        A, B -> strings -> single variable. 

        queries -> C/D -> find ans

        if variable not a part of equations -> then -1
        
        Valid Inputs -> no division by 0. 

        Match: Graph -> Dfs -> because we need to traverse throgh the equations -> and calculate the queries. 

        Plan:

        First Create a graph -> put A/ B -> val
        B/A = 1/val 
        for all the equations. 

        Now after creating the graph -> traverse the queries. if variables in queries -> not in equations -> return -1. 
        else start dfs from numerator, and we have to reach till numerator == denominator. 
        When they are equal -> we return ratio. 

        in each dfs, we also give ratio as parameter. And while traversing through the graphs -> multiply ratio by graph value of current num and neighbor we are traversing. 

        because. 

        a/d = a/b * b/d -> so we are following the same principle here. 
        '''

        graph = defaultdict(dict)

        for i, eqn in enumerate(equations):
            num, denom = eqn
            graph[num][denom] = values[i]
            graph[denom][num] = 1/values[i]

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
        
        division = []
        for num, denom in queries:
            if num in graph and denom in graph:
                division.append(dfs(num, denom, 1, {num}))
            else:
                division.append(-1)
        
        return division

        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
