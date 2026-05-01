class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l, m, n = len(s1), len(s2), len(s3)
        dp = {}
        def dfs(i, j, k):
            if k == n:
                return i == l and j == m
            if (i, j, k) in dp:
                return dp[(i, j , k)]
            res = False
            if i < l and s3[k] == s1[i]:
                if dfs(i + 1, j, k + 1):
                    res = True
                    return True
            if j < m and s3[k] == s2[j] :
                if dfs(i, j + 1, k + 1):
                    res = True
                    return True
            dp[(i, j, k)] = res
            return False
        
        return dfs(0, 0, 0)