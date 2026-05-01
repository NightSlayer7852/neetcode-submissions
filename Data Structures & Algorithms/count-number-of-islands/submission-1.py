class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            grid[r][c] = "0"
            
            while q:
                x, y = q.popleft()
                dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in dirs:
                    nr = x + dr
                    nc = y + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1" :
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    res += 1
        return res