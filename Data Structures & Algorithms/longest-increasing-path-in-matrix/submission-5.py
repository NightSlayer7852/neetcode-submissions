from functools import lru_cache
import sys

sys.setrecursionlimit(10 ** 6)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dfs(r, c):
            res = 1
            # if r + 1 < rows and matrix[r + 1][c] > matrix[r][c]:
            #     res = max(res, 1 + dfs(r + 1, c))
            # if r - 1 >= 0 and matrix[r - 1][c] > matrix[r][c]:
            #     res = max(res, 1 + dfs(r - 1, c))
            # if c + 1 < cols and matrix[r][c + 1] > matrix[r][c]:
            #     res = max(res, 1 + dfs(r, c + 1))
            # if c - 1 >= 0 and matrix[r][c - 1] > matrix[r][c]:
            #     res = max(res, 1 + dfs(r, c - 1))
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    res = max(res, 1 + dfs(nr, nc))
            return res
        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j))
        return res
