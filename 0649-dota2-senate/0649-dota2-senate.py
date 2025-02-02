class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        rq = deque()
        dq = deque()

        for i in range(len(senate)):
            if senate[i] == 'R':
                rq.append(i)
            else:
                dq.append(i)
        

        while rq and dq:
            if rq[0] < dq[0]:
                dq.popleft()
                rq.append(rq.popleft() + len(senate))
            else:
                rq.popleft()
                dq.append(dq.popleft() + len(senate))
        
        return 'Radiant' if rq else 'Dire'