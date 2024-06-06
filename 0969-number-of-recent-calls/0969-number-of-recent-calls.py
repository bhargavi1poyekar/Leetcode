class RecentCounter:
    '''
    Plan:

    1. Initialize an empty queue
    2. At every new ping:
        Check for requests t-3000 and remove them
    3. APpend current t
    3. Return len of current queue.

    '''
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:

        while self.queue and self.queue[0] < t-3000:
            self.queue.popleft()
        
        self.queue.append(t)
        return len(self.queue)


        

'''
Understand:



Match: queue





'''


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)