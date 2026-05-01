class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
    def search(self, word: str) -> bool:
        n = len(word)
        def dfs(j, root):
            if j == n:
                return root.word == True
            
            if word[j] == ".":
                for c in root.children:
                    if j < n and dfs(j + 1, root.children[c]):
                        return True
            elif word[j] in root.children:
                if j < n and dfs(j + 1, root.children[word[j]]):
                        return True
        
            return False
        
        return dfs(0, self.root)