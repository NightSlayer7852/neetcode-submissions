class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            new_perms = []
            for perm in res:
                for i in range(len(perm) + 1):
                    new_perm = perm.copy()
                    new_perm.insert(i, num)
                    new_perms.append(new_perm)
            res = new_perms
        return res