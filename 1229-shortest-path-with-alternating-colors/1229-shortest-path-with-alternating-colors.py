class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        # Assigning values to red and blue color
        RED = 0
        BLUE = 1

        # Creating Graph of graph of list -> To store color as well.
        graph = defaultdict(lambda:defaultdict(list))

        # Store the nghbrs in graphs. 
        for x, y in redEdges:
            graph[RED][x].append(y)
        
        for x, y in blueEdges:
            graph[BLUE][x].append(y)

        # We need to store node, color and steps in queue. 
        # start at node 0, with both red and blue as start. 
        queue = deque([(0, RED, 0), (0, BLUE, 0)])
        seen = {(0, RED), (0, BLUE)} # Put node 0 in seen with both RED and BLUE. 

        # Create final answer array, with max value, to be replaced later. 
        shortest_path = [float('inf') for x in range(n)]

        while queue:

            node, color, steps = queue.popleft()

            shortest_path[node] = min(shortest_path[node], steps)

            for nghbr in graph[color][node]:
                if (nghbr, 1-color) not in seen:
                    seen.add((nghbr, 1-color))
                    queue.append((nghbr, 1-color, steps+1))
        
        return [shortest if shortest!=float('inf') else -1 for shortest in shortest_path]

        