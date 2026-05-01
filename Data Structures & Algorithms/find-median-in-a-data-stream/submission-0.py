class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        self.m, self.n = 0, 0

    def addNum(self, num: int) -> None:
        if not self.maxheap:
            heapq.heappush(self.maxheap, -1 * num)
            self.m += 1
        else:
            if -1 * num > self.maxheap[0]:
                heapq.heappush(self.maxheap, -num)
                self.m += 1
            else:
                heapq.heappush(self.minheap, num)
                self.n += 1

         
        if self.n > self.m:
            x = heapq.heappop(self.minheap)
            self.n -= 1
            heapq.heappush(self.maxheap, -x)
            self.m += 1
        
        if self.m - self.n > 1:
            x = heapq.heappop(self.maxheap)
            self.m -= 1
            heapq.heappush(self.minheap, -x)
            self.n += 1

    def findMedian(self) -> float:
        if (self.m + self.n ) % 2 == 1:
            return -1 * self.maxheap[0]
        else:
            return (self.minheap[0] - self.maxheap[0]) / 2
