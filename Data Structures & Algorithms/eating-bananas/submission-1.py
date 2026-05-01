class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        def helper(k):
            res = 0
            for x in piles:
                res += math.ceil(float(x)/k)
            return res
        res = r
        while l <= r:
            m = (l + r) // 2
            hours = helper(m)
            if hours <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res