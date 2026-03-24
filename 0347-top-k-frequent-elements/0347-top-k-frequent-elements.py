class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # from collections import Counter
        cnt = Counter(nums)
        lst = [item for item in cnt.items()]
        lst.sort(key=lambda x: -x[1])
        ans = []
        for i in range(k):
            ans.append(lst[i][0])
        return ans