class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            g[b].append(a)
        
        colors = [0]*numCourses
        
        def dfs(x:int)->bool:
            colors[x] = 1
            for y in g[x]:
                if colors[y] == 1:
                    return True
                if colors[y] == 0:
                    if dfs(y):return True
            colors[x] = 2
            return False
        
        for i, c in enumerate(colors):
            if c == 0:
                if dfs(i):return False
        return True