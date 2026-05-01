class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        total = 1
        a = float('-inf')
        for num in nums:
            total = total * num
            a = max(a, total)
            if num == 0:
                total = 1
            
        total = 1
        b = float('-inf')
        for i in range(len(nums) - 1, -1 , -1):
            total = total * nums[i]
            b = max(b, total)
            if nums[i] == 0:
                total = 1
            
        print(a, b)
        return max(a, b)
        