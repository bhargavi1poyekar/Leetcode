class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def dfs(node):
            for nghbr in rooms[node]:
                if nghbr not in seen:
                    seen.add(nghbr)
                    dfs(nghbr)
        
        seen = {0}
        dfs(0)

        return len(seen) == len(rooms)