class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(i, m):
            if i < 0:
                return inf if m else 0
            if coins[i] > m:
                return dfs(i - 1, m)
            return min(dfs(i-1,m),dfs(i,m-coins[i])+1)
        ans = dfs(len(coins)-1,amount)

        return ans if ans < inf else -1
