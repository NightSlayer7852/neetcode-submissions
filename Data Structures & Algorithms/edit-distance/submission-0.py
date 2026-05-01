class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = {}
        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if (i, j) in dp:
                return dp[(i, j)]
            res = 0
            if word1[i] == word2[j]:
                res += dfs(i + 1, j + 1)
            else:
                res += min(
                    1 + dfs(i + 1, j),
                    1 + dfs(i, j + 1),
                    1 + dfs(i + 1, j + 1)
                )
            dp[(i, j)] = res
            return res
        return dfs(0, 0)