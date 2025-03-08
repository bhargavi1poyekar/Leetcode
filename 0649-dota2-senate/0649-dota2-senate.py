class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        r_queue = deque()
        d_queue = deque()

        n = len(senate)

        for i in range(n):
            if senate[i] == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)
        
        while r_queue and d_queue:
            if r_queue[0] < d_queue[0]:
                d_queue.popleft()
                r_queue.append(r_queue.popleft()+n)
            else:
                r_queue.popleft()
                d_queue.append(d_queue.popleft()+n)
        
        if r_queue:
            return 'Radiant'
        return "Dire"
        