class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = defaultdict(list)
        for x, y in prerequisites:
            hashmap[x].append(y)
        
        visited = set()
        def dfs(i):
            if i in visited:
                return False
            if hashmap[i] == []:
                return True
            visited.add(i)
            for x in hashmap[i]:
                if not dfs(x):
                    return False   
            visited.remove(i)
            hashmap[i] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True