class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res = float('-inf')
        l = 0
        count = defaultdict(int)
        for r in range(n):
            count[s[r]] += 1
            while l < n and k < (r - l + 1) - max(count.values()):
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res