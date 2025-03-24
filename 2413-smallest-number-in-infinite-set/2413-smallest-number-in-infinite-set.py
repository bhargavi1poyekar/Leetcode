class SmallestInfiniteSet:

    def __init__(self):
        self.min_heap = []
        self.add_back_hash = Counter()
        self.smallest = 1

    def popSmallest(self) -> int:
        if self.min_heap:
            del self.add_back_hash[self.min_heap[0]]
            return heapq.heappop(self.min_heap)
        min = self.smallest
        self.smallest += 1
        return min

    def addBack(self, num: int) -> None:
        if num not in self.add_back_hash and num < self.smallest:
            self.add_back_hash[num] += 1
            heapq.heappush(self.min_heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)