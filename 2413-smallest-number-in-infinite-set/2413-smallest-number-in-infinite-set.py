class SmallestInfiniteSet:

    def __init__(self):
        self.min_heap = []
        self.smallest = 1
        self.hash = {}

    def popSmallest(self) -> int:
        if self.min_heap:
            smallest = heapq.heappop(self.min_heap)
            del self.hash[smallest]
        else:
            smallest = self.smallest
            self.smallest += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.smallest and num not in self.hash:
            heapq.heappush(self.min_heap, num)
            self.hash[num] = 1


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)