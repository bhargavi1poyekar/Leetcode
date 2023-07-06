class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        rq,dq=deque(),deque()

        for i in range(len(senate)):
            if senate[i]=='R':
                rq.append(i)
            else:
                dq.append(i)
        ptr=0
        while rq and dq:
            if senate[ptr]=='R' and ptr in rq:
                dq.popleft()
                rq.append(rq.popleft())
            elif senate[ptr]=='D' and ptr in dq:
                rq.popleft()
                dq.append(dq.popleft())
            ptr=(ptr+1)%len(senate)
        
        return 'Radiant' if rq else 'Dire'