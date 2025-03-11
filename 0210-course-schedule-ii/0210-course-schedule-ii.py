class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0] * (numCourses)
        graph = defaultdict(list)
        
        for a, b in prerequisites:
            indegree[a] += 1
            graph[b].append(a)
        
        queue = deque()
        # seen = set()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                # seen.add(i)
                queue.append(i)

        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for nghbr in graph[node]:
                indegree[nghbr] -= 1
                if indegree[nghbr] == 0:
                    # seen.add(nghbr)
                    queue.append(nghbr)
        
        return order if len(order) == numCourses else []