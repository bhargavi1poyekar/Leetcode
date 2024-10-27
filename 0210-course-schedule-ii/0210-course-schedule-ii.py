class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0] * numCourses
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        course_order = []

        while queue:
            course = queue.popleft()
            course_order.append(course)

            for nghbr in graph[course]:
                indegree[nghbr] -= 1
                if indegree[nghbr] == 0:
                    queue.append(nghbr)

        return course_order 