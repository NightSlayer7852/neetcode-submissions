"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        if n < 2:
            return True
        intervals = sorted(intervals, key = lambda x : x.start)
        for i in range(1, n):
            if intervals[i - 1].end > intervals[i].start:
                return False
        return True