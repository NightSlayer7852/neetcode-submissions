class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        stack = []
        l, r = newInterval
        def merge(stack):
            if len(stack) < 2:
                return stack
            x, y = stack.pop()
            a, b = stack.pop()

            if x <= b:
                stack.append((min(a, x), max(b, y)))
            else:
                stack.append((a, b))
                stack.append((x, y))
            return stack
        inserted = 0
        for x, y in intervals:
            if x >= l and not inserted:
                stack.append((l, r))
                stack = merge(stack)
                inserted = 1
            stack.append((x, y))
            stack = merge(stack)
        if not inserted:
            stack.append((l, r))
            stack = merge(stack)

        return stack