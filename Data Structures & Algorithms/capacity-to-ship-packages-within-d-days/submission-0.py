class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        def helper(m):
            count = 1
            temp = m
            for w in weights:
                if w > temp:
                    temp = m
                    count += 1
                
                temp -= w
            return count
        res = float('inf')
        while l <= r:
            m = (l + r) // 2
            count = helper(m)
            if count <= days:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res