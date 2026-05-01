class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp = set()
        # def dfs(i):
        #     if i in dp:
        #         return
        #     if i == len(s):
        #         return True

        #     for w in wordDict:
        #         if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
        #             if dfs(i + len(w)):
        #                 return True
        #     dp.add(i)
        #     return False
        # return dfs(0)
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)]== w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]