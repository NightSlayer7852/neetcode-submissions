class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        total_sum = total/2
        def dfs(i,total):
            if i == len(nums):
                return False
            if total == total_sum:
                return True
            
            # road taken
            if dfs(i + 1, total + nums[i]) or dfs(i + 1, total):
                return True
            return False

        return dfs(0, 0)