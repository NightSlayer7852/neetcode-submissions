class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen, res = 0, 0
        for i in range(len(s)):
            # Odd length
            l, r = i, i
            while l>=0 and r<=len(s)-1 and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    res = l
                l -= 1
                r += 1

            #Even Length
            l, r = i, i + 1
            while l>=0 and r<=len(s)-1 and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    res = l
                l -= 1
                r += 1
        return s[res: res + resLen]