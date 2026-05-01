class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols, k = len(board), len(board[0]), len(word)
        visited = [[0] * cols for _ in range(rows)]
        def dfs(i, row, col):
            if i == k - 1:
                return True
            dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            visited[row][col] = 1
            for dr, dc in dirs:
                nr = row + dr
                nc = col + dc
                if nr in range(rows) and nc in range(cols) and board[nr][nc] == word[i + 1] and visited[nr][nc] == 0:
                    if dfs(i + 1, nr, nc):
                        visited[row][col] = 0
                        return True
                        
            visited[row][col] = 0
            return False
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(0,i,j):
                        return True
        return False