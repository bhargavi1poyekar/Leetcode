class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        num_visit = 0
        while queue:
            num_visit += 1
            node = queue.popleft()

            for nghbr in graph[node]:
                indegree[nghbr] -= 1
                if indegree[nghbr] == 0:
                    queue.append(nghbr)
        
        return num_visit == numCourses
