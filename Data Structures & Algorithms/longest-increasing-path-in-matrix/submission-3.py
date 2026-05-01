from functools import lru_cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dfs(r, c):
            res = 1
            if r + 1 < rows and matrix[r + 1][c] > matrix[r][c]:
                res = max(res, 1 + dfs(r + 1, c))
            if r - 1 >= 0 and matrix[r - 1][c] > matrix[r][c]:
                res = max(res, 1 + dfs(r - 1, c))
            if c + 1 < cols and matrix[r][c + 1] > matrix[r][c]:
                res = max(res, 1 + dfs(r, c + 1))
            if c - 1 >= 0 and matrix[r][c - 1] > matrix[r][c]:
                res = max(res, 1 + dfs(r, c - 1))
            
            return res
        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j))
        return res
