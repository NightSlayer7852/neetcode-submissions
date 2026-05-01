class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        q = deque()
        t = 0
        while maxHeap or q:
            t += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                if cnt + 1 < 0:
                    q.append([1 + cnt, t + n])
            if q and q[0][1] == t:
                heapq.heappush(maxHeap, q.popleft()[0])
        return t