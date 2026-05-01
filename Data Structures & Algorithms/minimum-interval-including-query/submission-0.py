class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for q in queries:
            minEle = float("inf")
            for x, y in intervals:
                print(x, q, y)
                if x <= q and q <= y:
                    minEle = min(minEle, y - x + 1)
            res.append(minEle if minEle != float("inf") else -1)
        return res