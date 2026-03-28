class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        last = {c : i for i, c in enumerate(s)}
        end = 0
        start = 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                ans.append(end-start+1)
                start = end + 1
        return ans