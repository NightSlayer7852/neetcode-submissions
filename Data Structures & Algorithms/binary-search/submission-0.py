class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(l, r):
            if l <= r:
                m = l + (r - l) // 2
                if nums[m] > target:
                    return binarySearch(l, m - 1)
                elif nums[m] < target:
                    return binarySearch(m + 1, r)
                else:
                    return m
            else:
                return -1
        
        return binarySearch(0, len(nums) - 1)