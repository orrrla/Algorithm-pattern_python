class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans =[]
        q=deque()

        for i, x in enumerate(nums):
            # 入
            while q and nums[q[-1]]<x:
                q.pop()
            q.append(i)
            # 出
            if i-q[0] >= k:
                q.popleft()
            # 记录答案
            if i >=k-1:
                ans.append(nums[q[0]])
        return ans