class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * (numCourses)
        graph = defaultdict(list)
        
        for a, b in prerequisites:
            indegree[a] += 1
            graph[b].append(a)
        
        queue = deque()
        seen = set()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                seen.add(i)
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for nghbr in graph[node]:
                indegree[nghbr] -= 1
                if nghbr not in seen and indegree[nghbr] == 0:
                    seen.add(nghbr)
                    queue.append(nghbr)
        
        return len(seen) == numCourses
                
