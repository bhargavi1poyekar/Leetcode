class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * (numCourses)
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        courses = []
        while queue:
            course = queue.popleft()
            courses.append(course)
            for nghbr in graph[course]:
                indegree[nghbr] -= 1
                if indegree[nghbr] == 0:
                    queue.append(nghbr)
        
        if len(courses) == numCourses:
            return courses
        return []