class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        n = len(rooms)
        seen = {0}

        def dfs(node):
            for nghbr in rooms[node]:
                if nghbr not in seen:
                    seen.add(nghbr)
                    dfs(nghbr)
        
        dfs(0)
        return len(seen) == n

