import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.min_heap = []
        self.alreadyPresent=Counter() # if once trying add back, now again trying addback the same element

    def popSmallest(self) -> int:
        if self.min_heap:
            self.alreadyPresent[self.min_heap[0]]=0
            return heapq.heappop(self.min_heap)
        else:
            min = self.curr
            self.curr += 1
            return min

    def addBack(self, num: int) -> None:
        if num < self.curr and self.alreadyPresent[num]==0:
            heapq.heappush(self.min_heap, num)
            self.alreadyPresent[num] = 1



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)