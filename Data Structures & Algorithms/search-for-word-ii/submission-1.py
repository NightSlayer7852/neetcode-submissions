class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        for word in words:
            self.addWord(word)
        
        res = []
        word = []
        visited = set()
        def dfs(r, c, root):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if board[r][c] not in root.children:
                return
            visited.add((r, c))
            next_node = root.children[board[r][c]]
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None
            if r + 1 in range(rows) and (r + 1, c) not in visited:
                dfs(r + 1, c , next_node)
            if r - 1 in range(rows) and (r - 1, c) not in visited:
                dfs(r - 1, c, next_node)
            if c + 1 in range(cols) and (r, c + 1) not in visited:
                dfs(r, c + 1, next_node)
            if c - 1 in range(cols) and (r, c - 1) not in visited:
                dfs(r, c - 1, next_node)
            visited.remove((r, c))
            return
            
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, self.root)
        return res