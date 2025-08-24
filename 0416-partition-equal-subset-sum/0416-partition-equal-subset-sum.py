class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 !=0:
            return False
        target = sum(nums)//2
        n=len(nums)
        @cache
        def dfs(i, c):
            if i<0 or c <0:
                return False
            if c==0:
                return True
            return dfs(i-1,c) or dfs(i-1,c-nums[i])
        return dfs(n-1,target)