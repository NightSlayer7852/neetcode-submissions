from functools import lru_cache

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        @lru_cache(None)
        def dfs(i, target):
            if target < 0:
                return 0
            if target == 0:
                return 1
            if i == len(nums):
                return target == 0
            res = 0
            for j in range(len(nums)):
                res += dfs(j, target - nums[j])
            return res

        return dfs(0, target)