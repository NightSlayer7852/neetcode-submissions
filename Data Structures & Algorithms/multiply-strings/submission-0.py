class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        m = len(num1)
        n = len(num2)
        for i in range(m):
            for j in range(n):
                res += int(num1[i]) * 10 **(m - i - 1) * int(num2[j]) * 10 **(n - j - 1)
        return str(res)