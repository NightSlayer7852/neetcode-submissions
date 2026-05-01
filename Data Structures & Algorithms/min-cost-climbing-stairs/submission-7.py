from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        @lru_cache(None)
        def dfs(i):
            if i >= n:
                return 0

            res = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return res

        return min(dfs(0), dfs(1))