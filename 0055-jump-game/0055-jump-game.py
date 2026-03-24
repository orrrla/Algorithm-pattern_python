class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        cover = 0
        for i, x in enumerate(nums):
            if i > cover: return False
            cover = max(cover,i+x)
            if cover >= n - 1:
                return True
        return False
