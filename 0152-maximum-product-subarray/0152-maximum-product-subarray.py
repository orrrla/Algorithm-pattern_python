class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = -inf
        f_max=f_min = 1
        for x in nums:
            f_max = max(f_max*x,f_min*x,x)
            f_min = min(f_max*x,f_min*x,x)
            ans = max(ans,f_max)
        return ans