class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}
        def dfs(r, c, prev):
            if not r in range(rows) or not c in range(cols) or matrix[r][c] <= prev:
                return 0
            if (r, c ) in dp:
                return dp[(r, c)]
            res = 1 + max(
                dfs(r - 1, c, matrix[r][c]),
                dfs(r, c - 1, matrix[r][c]),
                dfs(r + 1, c, matrix[r][c]),
                dfs(r, c + 1, matrix[r][c])
            )

            
            dp[(r, c)] = res

            return res
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c, float('-inf')))
        return res