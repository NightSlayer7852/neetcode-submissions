"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        intervals.sort(key = lambda x : x.start)
        if n == 0:
            return 0
        minheap = [intervals[0].end]

        res = 1
        
        for interval in intervals[1:]:
            x, y = interval.start, interval.end
            if minheap[0] <= x:
                heapq.heappop(minheap)
            else:
                res += 1
            heapq.heappush(minheap, y)
            
        return res
        
        