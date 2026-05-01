class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()
        q = collections.deque()
        for r in range(rows):
            if board[r][0] == "O":
                visited.add((r, 0))
            if board[r][cols - 1] == "O":
                visited.add((r, cols - 1))
        
        for c in range(cols):
            if board[0][c] == "O":
                visited.add((0, c))
            if board[rows - 1][c] == "O":
                visited.add((rows - 1, c))
        for x in visited:
            q.append(x)
        print(q)

        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                board[x][y] = "P"

                dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in dirs:
                    nr, nc = x + dr, y + dc
                    if nr in range(rows) and nc in range(cols) and board[nr][nc] == "O" and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
        print(board)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "P":
                    board[r][c] = "O"
        