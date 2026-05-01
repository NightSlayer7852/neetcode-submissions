class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxleft = [0]*n
        maxright = [0]*n

        for i in range(1,n):
            maxleft[i] = max(maxleft[i - 1], height[i - 1])

        for i in range(n - 2, -1, -1):
            maxright[i] = max(maxright[i + 1], height[i + 1])

        res = 0
        for i in range(n):
            x = min(maxleft[i], maxright[i]) - height[i]
            if x>0:
                res+=x
        return res