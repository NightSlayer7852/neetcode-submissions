class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = {}
        def dfs(i, j):
            if i >= m and j >= n:
                return True
            if j >= n:
                return False
            if (i, j) in dp:
                return dp[(i, j)]

            if i < m and (s[i] == p[j] or p[j] == "."):
                if j + 1 < n and p[j + 1] == "*":
                    dp[(i, j)] = dfs(i + 1, j) or dfs(i, j + 2)
                else:
                    dp[(i, j)] = dfs(i + 1, j + 1)
                    
            else:
                if j + 1 < n and p[j + 1] == "*":
                    dp[(i, j)] = dfs(i, j + 2)
                else:
                    dp[(i, j)] = False

            return dp[(i, j)]
        return dfs(0, 0)