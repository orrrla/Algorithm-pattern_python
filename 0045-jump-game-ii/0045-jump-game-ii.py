class Solution:
    def jump(self, nums: List[int]) -> int:
        cur = 0
        nxt = 0
        ans = 0
        for i in range(len(nums)-1):
            nxt = max(nxt,i+nums[i])
            if i == cur:
                cur = nxt
                ans+=1
        return ans 