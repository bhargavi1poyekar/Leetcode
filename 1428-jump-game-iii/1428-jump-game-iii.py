class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        def dfs(node):
            if arr[node] == 0:
                return True

            for nghbr in (node+arr[node], node-arr[node]):
                if 0<=nghbr<len(arr) and nghbr not in seen:
                    seen.add(nghbr)
                    if dfs(nghbr):
                        return True
            
            return False
        
        seen = {start}
        return dfs(start)



