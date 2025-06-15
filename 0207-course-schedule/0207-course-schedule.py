class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        indegree = [0] * (numCourses)
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        numCount = 0
        while queue:
            course = queue.popleft()
            numCount += 1
            for nghbr in graph[course]:
                indegree[nghbr] -= 1
                if indegree[nghbr] == 0:
                    queue.append(nghbr)
        
        return numCount == numCourses
