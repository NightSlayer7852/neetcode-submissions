class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for x, y in points:
            heapq.heappush(maxheap, [-(math.sqrt(x**2 + y**2)),[x, y]])
        
        for i in range(len(points) - k):
            heapq.heappop(maxheap)
        
        return [ y for _,y in maxheap]
        