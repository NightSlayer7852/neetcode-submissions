class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort( key = lambda x:x[0])
        stack = []

        def merge(stack, n):
            if n < 2:
                return stack, n
            x, y = stack[-1]
            a, b = stack[-2]
            if x <= b:
                stack.pop()
                stack.pop()
                n -= 2
                stack.append([min(a, x), max(b, y)])
                n  += 1
            return stack, n
        n = 0
        for x, y in intervals:
            stack.append([x, y])
            n += 1
            stack, n = merge(stack, n)
        return stack