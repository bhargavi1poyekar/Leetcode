class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        '''
        Understand:

        2 parties -> Radiant and Dire
        Voting -> Round based procedure. 
        2 rights:
            ban one senator
            announce victory -> if all senators from other party has lost.

        'R' and 'D' -> only 2 chars in the given senate arr. 
        starts from first senator -> round based till one party wins. 

        Return -> who wins? 

        Match:
        since voting sounds similar to first come first serve. Beacuse the senator who is first -> can ban other senator -> we can use queue. 

        Plan:
        2 queue -> each for a party -> stores indices of where a senator is in the senate arr. 

        then will check first indices of both the queues
        one with less index -> wins and bans the other
        remove the one with greater index from queue. 
        and as it is a round based procedure, the one who one, again gets a chance, but we will pop and push it again in the queue with updated index if i+n. 
        We will do this, till one of the queue gets empty. 
        so at the end, the queue that is not empty -> will win. 
        '''

        # Implement

        # Pushing indexes to queues
        R_queue = deque()
        D_queue = deque()
        n = len(senate)

        for i, party in enumerate(senate):
            if party == 'R':
                R_queue.append(i)
            else:
                D_queue.append(i)
        
        # Voting Procedure

        # Till one of the queue gets empty, continue voting.
        while R_queue and D_queue:
            # R gets voting right
            if R_queue[0] < D_queue[0]:
                D_queue.popleft() # ban that senator
                R_queue.append(R_queue.popleft() + n) 
                # pop and add to the queue with i + n index

            # D gets voting right
            else:
                R_queue.popleft() # ban that senator
                D_queue.append(D_queue.popleft() + n) 
                # pop and add to the queue with i + n index
        
        if R_queue: # if R_queue not empty
            return 'Radiant'
        return 'Dire' # else D won

        '''
        EG: RDRRDRDD

        n = 8
        R_queue = [8, 10, 11, 13]
        D_queue = []

        0 < 1 # R won
        2 < 4 # R won
        3 < 6 # R won
        5 < 7 # R won

        D is empty -> Radiant wins. 

        # Evaluate:

        Time Complexity: O(n) -> adding indices to queue. 
                         O(n) -> total votings
        Space Complexity: O(n)
        '''
        

