class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        return curr

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for s in strs:
            trie.addWord(s)
        curr = trie.root
        res = []
        while len(curr.children) == 1 and not curr.word:
            for c in curr.children:
                res.append(c)
                curr = curr.children[c]
        
        return "".join(res)
