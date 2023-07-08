class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        rq,dq=deque(),deque() # queues for both parties

        # Adding the indexes in respective queues.
        for i in range(len(senate)):
            if senate[i]=='R':
                rq.append(i)
            else:
                dq.append(i)
        
        # until one of the party is empty (all senators are banned from a party)
        while rq and dq:
            if rq[0]<dq[0]: # Radiant senator turn is before dire
                dq.popleft() # Ban dire senator
                rq.append(rq.popleft()+len(senate)) # next turn after n 
            else: # dire's turn
                rq.popleft() # ban radiant
                dq.append(dq.popleft()+len(senate))


        return 'Radiant' if rq else 'Dire'
