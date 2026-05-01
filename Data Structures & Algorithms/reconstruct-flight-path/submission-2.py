class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        tickets.sort()
        for u,v in tickets:
            adjList[u].append(v)
            
        res = ["JFK"]

        def dfs(u):
            if len(res) == len(tickets) + 1:
                return True
            temp = adjList[u]
            for i, v in enumerate(temp):
                res.append(v)
                adjList[u].pop(i)
                if dfs(v): return True
                res.pop()
                adjList[u].insert(i, v)
            return False
        dfs("JFK")
        return res