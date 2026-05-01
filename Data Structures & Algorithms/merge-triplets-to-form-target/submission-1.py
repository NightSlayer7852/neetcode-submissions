class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0, 0, 0]
        for x, y, z in triplets:
            nx, ny, nz = max(res[0], x), max(res[1], y), max(res[2], z)
            if nx <= target[0] and ny <= target[1] and nz <= target[2]:
                res = [nx, ny, nz]
        return res == target