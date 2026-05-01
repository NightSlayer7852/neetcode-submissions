class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            return 1 + dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c)
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
                    grid[i][j] == 0

        return res