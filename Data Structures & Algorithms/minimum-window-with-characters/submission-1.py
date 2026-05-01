class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        resLen = float('inf')
        freqt = [0] * 256
        for c in t:
            freqt[ord(c)] += 1
        freqs = [0] * 256
        l = 0
        for r in range(len(s)):
            freqs[ord(s[r])] += 1
            while all(freqs[i] >= freqt[i] for i in range(256)):
                if r - l + 1 < resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                freqs[ord(s[l])] -= 1
                l += 1
        return res