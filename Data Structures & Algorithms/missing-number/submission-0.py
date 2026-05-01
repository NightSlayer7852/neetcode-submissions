class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) + 1):
            res ^= i
        res1 = 0
        for x in nums:
            res1 ^= x
        return res^res1