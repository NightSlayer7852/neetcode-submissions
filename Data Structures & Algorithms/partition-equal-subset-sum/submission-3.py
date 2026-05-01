from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        total_sum = total/2
        @lru_cache(None)
        def dfs(i,total):
            if total == total_sum:
                return True

            if i == len(nums) or total > total_sum:
                return False
            
            return dfs(i + 1, total + nums[i]) or dfs(i + 1, total)

        return dfs(0, 0)