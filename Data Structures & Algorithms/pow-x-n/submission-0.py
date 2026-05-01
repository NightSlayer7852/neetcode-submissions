class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        res = 1
        flag = False
        if n < 0:
            flag = True
            n *= -1
        for i in range(n):
            res *= x
        
        if flag:
            return 1/res
        else:
            return res