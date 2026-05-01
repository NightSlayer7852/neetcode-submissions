class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append([v, w])
        res = float('inf')
        def dfs(u, k, dist):
            nonlocal res
            if k < 0:
                return
            if u == dst:
                res = min(res, dist)
            for v, w in adj[u]:
                dfs(v, k - 1, dist + w)
            return
        dfs(src, k + 1, 0)
        return -1 if res == float("inf") else res
