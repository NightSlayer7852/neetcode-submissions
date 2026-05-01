class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        l = 0
        total = 0
        res = float('inf')
        for r in range(n):
            total += nums[r]
            while total >= target:
                print(res)
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return res if res != float('inf') else 0