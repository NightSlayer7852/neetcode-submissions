from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        @lru_cache(None)
        def dfs(i):
            if i == n:
                return 1
            
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            
            return res
        return dfs(0)