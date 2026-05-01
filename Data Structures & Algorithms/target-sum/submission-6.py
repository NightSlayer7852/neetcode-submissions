from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # @lru_cache(None)
        # def dfs(i, total):
        #     if i == n:
        #         return total == target
            
        #     res = dfs(i + 1, total + nums[i])
        #     res += dfs(i + 1, total - nums[i])
        #     return res
        # return dfs(0, 0)

        offset = sum(nums)
        dp = [[0] * (2 * offset  + 1) for _ in range(n + 1)]
        if abs(target) > offset:
            return 0
        dp[n][target + offset] = 1
        for i in range(n - 1, - 1, -1):
            for j in range(-offset, offset + 1):
                dp[i][j + offset] = 0
                if -offset <= j + nums[i] <= offset:
                    dp[i][j + offset] += dp[i + 1][j + offset + nums[i]]
                if -offset <= j - nums[i] <= offset:
                    dp[i][j + offset] += dp[i + 1][j + offset - nums[i]]

        return dp[0][offset]