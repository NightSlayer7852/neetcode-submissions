class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        memo = {}
        def dfs(i):
            if i == n - 1:
                return 0
            if i in memo:
                return memo[i]
            res = float('inf')
            minRes = float('inf')
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                res = 1 + dfs(j)
                minRes = min(res, minRes)
            memo[i] = minRes
            return minRes
        return dfs(0)