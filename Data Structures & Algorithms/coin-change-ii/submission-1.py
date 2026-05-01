class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        res = 0
        coins.sort()
        dp = {}
        def dfs(i, total):
            if total == 0:
                return 1
            if i >= n:
                return 0
            if (i, total) in dp:
                return dp[(i, total)]
            res = 0
            if total >= coins[i]:
                res = dfs(i, total - coins[i]) + dfs(i + 1, total) 
            dp[(i, total)] = res
            return res

        return dfs(0, amount)