class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid),len(grid[0])

        def dfs(i,j):
            if i < 0 or i >=m or j < 0 or j >= n or grid[i][j]!='1':
                return
            grid[i][j] = '2'
            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i-1,j)

        
        ans = 0
        for i, row in enumerate(grid):
            for j,col in enumerate(row):
                if grid[i][j]=='1':
                    dfs(i,j)
                    ans+=1
        return ans
                    