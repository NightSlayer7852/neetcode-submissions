class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        
        for u, v, w in times:
            adjList[u].append((v, w))
        
        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        pq = [(0, k)]
        while pq:
            curr_dist, u = heapq.heappop(pq)
            if curr_dist > dist[u]:
                continue
            
            for v, w in adjList[u]:
                new_dist = curr_dist + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
        max_dist = max(dist[1:])
        
        return -1 if max_dist == float("inf") else max_dist