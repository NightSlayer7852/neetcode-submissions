class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minele = min(nums)
        n = len(nums)
        if 1 not in nums:
            return 1
        offset = -1
        for num in nums:
            temp = num
            while temp != 0.5:
                if 0 <= temp + offset < n:
                    temp2 = nums[temp + offset]
                    nums[temp + offset] = 0.5
                    temp = temp2
                else:
                    break
        res = -1
        zero = 0
        for i in range(n):
            if nums[i] != 0.5:
                if i - offset != 0:
                    zero = 1
                    res = i
                    break
        print(res)
        if res == -1:
            return n - offset
        else:
            return res - offset