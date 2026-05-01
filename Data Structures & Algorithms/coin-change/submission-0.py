class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)

        def dfs(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            if dp[rem] != -1:
                return dp[rem]

            dp[rem] = min(1 + dfs(rem - c) for c in coins)
            return dp[rem]

        res = dfs(amount)
        return -1 if res == float('inf') else res
