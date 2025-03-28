import heapq
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        def isValid(row, col):
            return 0 <= row < Row and 0 <= col < Col

        Row = len(grid)
        Col = len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        sorted_queries = sorted([val, idx] for idx, val in enumerate(queries))

        min_heap = []
        seen = set()

        total_points = 0

        heapq.heappush(min_heap, (grid[0][0], 0, 0))
        seen.add((0, 0))
        result = [0] * len(queries)

        for query_val, query_idx in sorted_queries:
            while min_heap and min_heap[0][0] < query_val:
                val, row, col = heapq.heappop(min_heap)

                total_points += 1

                for dx, dy in directions:
                    nextr, nextc = row + dx, col + dy
                
                    if isValid(nextr, nextc) and (nextr, nextc) not in seen:
                        heapq.heappush(min_heap, (grid[nextr][nextc], nextr, nextc))
                        seen.add((nextr, nextc))
            
            result[query_idx] = total_points
        
        return result