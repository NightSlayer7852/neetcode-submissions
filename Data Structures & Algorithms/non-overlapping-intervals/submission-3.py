class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        res = 1
        intervals.sort(key = lambda x : x[1])
        temp = intervals[0][1]
        for x, y in intervals[1:]:
            if temp <= x:
                res += 1
                temp = y
            
        return n - res