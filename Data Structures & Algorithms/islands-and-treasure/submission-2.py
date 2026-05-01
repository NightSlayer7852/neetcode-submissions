class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        
        while q:
            r, c, w = q.popleft()
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = w + 1
                    q.append((nr, nc, w + 1))
        
        