class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = [0]*n
        ans = []

        def dfs(i,s):
            if i == n:
                ans.append(path.copy())
            else:
                for x in s:
                    path[i] = x
                    dfs(i+1,s-{x})
        
        dfs(0,set(nums))
        return ans