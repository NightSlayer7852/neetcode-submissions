class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n  = len(nums)
        res, maxVal = [], -1001
        count = Counter(nums[:k])
        for x in count.keys():
            maxVal = max(x, maxVal)
        res.append(maxVal)

        l = 0
        for r in range(k,n):
            
            count[nums[r]] = count.get(nums[r], 0) + 1
            maxVal = max(nums[r], maxVal)
            count[nums[l]] -= 1
            if nums[l] == maxVal and count[nums[l]] == 0:
                maxVal = -1001
                for x in count.keys():
                    if count[x] > 0:
                        maxVal = max(x, maxVal)
            res.append(maxVal)
            l += 1
    
        return res