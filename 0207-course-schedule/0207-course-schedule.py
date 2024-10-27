class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses

        graph = defaultdict(list)

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        num_visit = 0
        while queue:
            num_visit += 1
            course = queue.popleft()
            for nghbr in graph[course]:
                indegree[nghbr] -= 1
                if indegree[nghbr] == 0:
                    queue.append(nghbr)
        
        return num_visit == numCourses


