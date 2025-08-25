class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # @cache
        # def dfs(i,j):
        #     if i<0 or j<0:
        #         return inf
        #     if i==0 and j==0:
        #         return grid[i][j]
        #     return min(dfs(i-1,j),dfs(i,j-1))+grid[i][j]

        # return dfs(m-1,n-1)
        for j in range(1,n):
            grid[0][j]+=grid[0][j-1]
        for i in range(1,m):
            grid[i][0]+=grid[i-1][0]
        
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j]
        return grid[m-1][n-1]