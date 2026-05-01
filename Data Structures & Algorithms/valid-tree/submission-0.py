class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
        
        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)
            for x in adjList[i]:
                if x == prev:
                    continue
                if not dfs(x, i):
                    return False
            return True
        return dfs(0, -1) and n == len(visited)