class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if not trust and n == 1:
            return 1

        # indegree = [0] * n
        indegree = Counter()

        for a, b in trust:
            indegree[b] += 1
            indegree[a] -= 1
        
        print(indegree)
        for person in indegree:
            if indegree[person] == n-1:
                return person
        
        return -1