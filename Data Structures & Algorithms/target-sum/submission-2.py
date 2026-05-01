from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @lru_cache(None)
        def dfs(i, total):
            if i == n:
                return total == target
            
            res = dfs(i + 1, total + nums[i])
            res += dfs(i + 1, total - nums[i])
            return res
        return dfs(0, 0)