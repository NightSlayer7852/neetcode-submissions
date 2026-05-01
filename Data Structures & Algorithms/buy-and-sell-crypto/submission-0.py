class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minleft =[100]*n
        maxright =[0]*n
        x = 100
        for i in range(n):
            x = min(x,prices[i])
            minleft[i] = x

        x = 0
        for i in reversed(range(n)):
            x = max(x,prices[i])
            maxright[i] = x
        
        res = 0

        for i in range(n):
            res = max(res, maxright[i] - minleft[i])
        return res