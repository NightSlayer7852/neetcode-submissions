from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # @lru_cache(None)
        # def dfs(i, amt):
        #     if i >= n or amt > amount:
        #         return 0
            
        #     if amt == amount:
        #         return 1
            
        #     res = dfs(i, amt + coins[i])
        #     res += dfs(i + 1, amt)
        
        #     return res
        # return dfs(0, 0)
    
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][amount] = 1

        for i in range(n - 1, -1, -1):
            for amt in range(amount, -1, -1):
                dp[i][amt] = 0
                if amt + coins[i] <= amount:
                    dp[i][amt] = dp[i][amt + coins[i]]
                dp[i][amt] += dp[i + 1][amt]
                
        return dp[0][0]