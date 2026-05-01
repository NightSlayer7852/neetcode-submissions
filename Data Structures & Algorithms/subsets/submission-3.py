class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            temp = []
            for x in res:
                temp.append(x + [n])
            res.extend(temp)
        return res