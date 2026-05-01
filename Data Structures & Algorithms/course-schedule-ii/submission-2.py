class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)

        for x, y in prerequisites:
            preMap[x].append(y)

        res = []
        visited, cycle = set(), set()
        def dfs(i):
            if i in cycle:
                return False

            if i in visited:
                return True
            
            cycle.add(i)
            for x in preMap[i]:
                if not dfs(x):
                    return False
                
            cycle.remove(i)
            visited.add(i)
            res.append(i)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res