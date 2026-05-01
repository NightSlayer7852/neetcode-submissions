class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        hashset = set(nums)
        res = 1
        for x in nums:
            length = 1
            if x-1 in hashset:
                continue

            while(x+1 in hashset):
                x+=1
                length+=1
            
            res = max(res,length)
        return res