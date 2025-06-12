class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        Rq = deque()
        Dq = deque()
        n = len(senate)

        for i in range(len(senate)):
            if senate[i] == 'R':
                Rq.append(i)
            else:
                Dq.append(i)
        
        while Rq and Dq:
            if Rq[0] < Dq[0]:
                Dq.popleft()
                Rq.append(n + Rq.popleft())
            else:
                Rq.popleft()
                Dq.append(n + Dq.popleft())
        
        if Rq:
            return 'Radiant'
        else:
            return 'Dire'