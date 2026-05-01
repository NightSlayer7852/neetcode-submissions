class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0, 1, 1, 2]
        k = 2
        for i in range(4, n + 1):
            if k == i//2:
                k = i
            res.append(res[i-k] + 1)
        return res[:n + 1]