class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for i in range(n):
            for j in range(amount + 1):
                if j >= coins[i]:
                    dp[j] = dp[j] + dp[j - coins[i]]
        return dp[amount
        
        ]