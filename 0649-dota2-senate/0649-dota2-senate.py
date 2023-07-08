class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        rq,dq=deque(),deque()

        for i in range(len(senate)):
            if senate[i]=='R':
                rq.append(i)
            else:
                dq.append(i)
            
        idx=0
        while rq and dq:
            if idx in rq:
                dq.popleft()
                rq.append(rq.popleft())
            elif idx in dq:
                rq.popleft()
                dq.append(dq.popleft())
            idx=(idx+1)%len(senate)
        
        return 'Radiant' if rq else 'Dire'
