class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        graph = defaultdict(list)

        for eqn in equations:
            if eqn[1] == '=':
                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[3]) - ord('a')
                graph[x].append(y)
                graph[y].append(x)

        def dfs(node, comp):
            if components[node] == -1:
                components[node] = comp
                
                for nghbr in graph[node]:
                    if components[nghbr] == -1:
                        dfs(nghbr, comp)

        components = [-1] * 26
        for i in range(26):
            if components[i] == -1:
                dfs(i, i)
        
        for eqn in equations:
            if eqn[1] == '!':
                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[3]) - ord('a')

                if components[x] == components[y]:
                    return False
        
        return True