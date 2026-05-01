class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        n = len(heights)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                res = max(res, height * (i - idx))
                start = idx
            stack.append((start, h))

        for i, h in stack:
            res = max(res, h * (n - i))
        return res