from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @lru_cache(None)
        def dfs(i, amt):
            if i >= n or amt > amount:
                return 0
            
            if amt == amount:
                return 1
            
            res = dfs(i, amt + coins[i])
            res += dfs(i + 1, amt)
        
            return res
        return dfs(0, 0)