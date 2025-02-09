class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
    
        def find_nghbrs(code):
            ans = []
            for i in range(4):
                num = int(code[i]) # each wheel 
                for change in [-1, 1]:
                    x = (num + change) % 10 # for 9 to turn to 0
                    ans.append(code[:i] + str(x) + code[i+1:])
            return ans

        start = "0000"

        if start in deadends:
            return -1

        seen = set(deadends)
        seen.add(start)

        queue = deque([(start, 0)])

        while queue:
            code, steps = queue.popleft()
            if code == target:
                return steps
            
            for nghbr in find_nghbrs(code):
                if nghbr not in seen:
                    seen.add(nghbr)
                    queue.append((nghbr, steps + 1))
        
        return -1

