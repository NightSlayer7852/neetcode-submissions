class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1    
        count = 0
        while q and fresh > 0:
            for i in range(len(q)):
                dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            count += 1
        return count if fresh == 0 else -1