class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        n=len(rooms)

        def dfs(node):

            for key in rooms[node]:
                if key not in seen:
                    seen.add(key)
                    dfs(key)
        
        seen={0}

        dfs(0)

        
        return len(seen)==n





        