class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        visited = set()
        
        def dfs(r, c, prev):
            if not r in range(rows) or not c in range(cols) or (r, c) in visited or matrix[r][c] <= prev:
                return 0
            visited.add((r, c))
            res = 1 + max(
                dfs(r - 1, c, matrix[r][c]),
                dfs(r, c - 1, matrix[r][c]),
                dfs(r + 1, c, matrix[r][c]),
                dfs(r, c + 1, matrix[r][c])
            )
            visited.remove((r, c))
            return res
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c, float('-inf')))
        return res