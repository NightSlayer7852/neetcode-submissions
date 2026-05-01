class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = []
        for i in range(n):
            for j in range(i + 1, n):
                dist.append([abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j])
        dist.sort()
        res = 0
                
        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)
        
        def find(n):
            if n !=par[n]:
                return find(par[n])
            return par[n]
        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p2] += rank[p1]
            else:
                par[p1] = p2
                rank[p1] += rank[p2]
            return True
        for w, x, y in dist:
            if union(x, y):
                res += w

        return res