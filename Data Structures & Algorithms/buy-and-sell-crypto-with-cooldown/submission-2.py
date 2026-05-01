from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # @lru_cache(None)
        # def dfs(i, buying):
        #     if i >= n:
        #         return 0
            
        #     res = dfs(i + 1, buying)
        #     if buying:
        #         res = max(res,dfs(i + 1, not buying) - prices[i])
        #     else:
        #         res = max(res,dfs(i + 2, not buying) + prices[i])
        #     return res

        # return dfs(0, True)

        dp = [[0] * 2 for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for buying in [True, False]:
                if buying:
                    buy = dp[i + 1][False] - prices[i] if i + 1 < n else -prices[i]
                    cooldown = dp[i + 1][True] if i + 1 < n else 0
                    dp[i][1] = max(buy, cooldown)
                else:
                    sell = dp[i + 2][True] + prices[i] if i + 2 < n else prices[i]
                    cooldown = dp[i + 1][False] if i + 1 < n else 0
                    dp[i][0] = max(sell, cooldown)
        return dp[0][1]