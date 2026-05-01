from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache(None)
        def dfs(i, buying):
            if i >= n:
                return 0
            
            res = dfs(i + 1, buying)
            if buying:
                res = max(res,dfs(i + 1, not buying) - prices[i])
            else:
                res = max(res,dfs(i + 2, not buying) + prices[i])
            return res

        return dfs(0, True)