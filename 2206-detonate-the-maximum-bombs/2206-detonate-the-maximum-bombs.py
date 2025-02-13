class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        def dfs(node, seen):
            for nghbr in graph[node]:
                if nghbr not in seen:
                    seen.add(nghbr)
                    dfs(nghbr, seen)

            return len(seen)

        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]

                if r1 ** 2 >= (x1-x2)**2 + (y1-y2)**2:
                    graph[i].append(j)
        
        max_detonate = 0 

        for bomb in range(len(bombs)):
            max_detonate = max(max_detonate, dfs(bomb, {bomb}))
        
        return max_detonate


