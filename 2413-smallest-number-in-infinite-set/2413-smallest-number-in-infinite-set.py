class SmallestInfiniteSet:

    def __init__(self):
        self.min_heap = []
        self.curr = 1
        self.add_back = Counter()

    def popSmallest(self) -> int:
        if self.min_heap:
            self.add_back[self.min_heap[0]] -= 1
            return heapq.heappop(self.min_heap)
        else:
            min = self.curr
            self.curr += 1
            return min

    def addBack(self, num: int) -> None:
        if num < self.curr and not self.add_back[num]:
            self.add_back[num] += 1
            heapq.heappush(self.min_heap, num) 
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)