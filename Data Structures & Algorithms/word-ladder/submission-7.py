class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n = len(beginWord)
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(n):
                pattern = word[:i] + '*' + word[i + 1:]
                nei[pattern].append(word)
        
        q = collections.deque([beginWord])
        visited = set([beginWord])

        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(n):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0