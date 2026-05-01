class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        part = []
        def dfs(i):
            if i >=len(s):
                res.append(part.copy())

            for j in range(i, n):
                x = s[i : j + 1]
                if x == x[:: -1]:
                    part.append(x)
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res