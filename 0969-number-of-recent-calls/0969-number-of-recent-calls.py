class RecentCounter:

    '''
    Understand: Given recent Counter. 

    initializes -> counter with 0 requests
    ping -> adds a new req at time t (ms).

    and returns the num requests happened in past 3000 ms.

    Match: Queue. t is strictly larger, so we don't need request with time < t-3000

    We can remove the oldest requests. 

    Plan:
    in ping, remove all the requests with time < t - 3000. 
    and then add t, and return length of queue. 
    '''

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int: 
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        self.queue.append(t)
        return len(self.queue)
    
    '''
    Time Complexity: O(N)
    Space COmplexity: O(N)
    '''

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)