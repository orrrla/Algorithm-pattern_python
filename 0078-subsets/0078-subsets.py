class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []
        n = len(nums)

        def dfs(i):
            
            if i == n:
                ans.append(path.copy())
                return
            # 不选
            dfs(i+1)
            # 选 i
            path.append(nums[i])
            dfs(i+1)
            path.pop() # 恢复现场

        dfs(0)
        return ans