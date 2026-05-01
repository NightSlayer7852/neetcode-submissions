class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        q = collections.deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        dist = 0
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                grid[x][y] = dist
                for dr, dc in dirs:
                    nr, nc = x + dr, y + dc
                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited and grid[nr][nc]!= -1:
                        q.append((nr,nc))
                        visited.add((nr, nc))
            dist += 1