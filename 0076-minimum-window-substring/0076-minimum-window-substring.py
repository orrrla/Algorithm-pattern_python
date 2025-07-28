class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_s = Counter()
        cnt_t = Counter(t)

        ans_left,ans_right=-1,len(s)
        left = 0
        for right, x in enumerate(s):
            cnt_s[x] += 1
            while cnt_s >= cnt_t:
                if right - left < ans_right-ans_left:
                    ans_left,ans_right=left,right
                cnt_s[s[left]]-=1
                left+=1
        return s[ans_left:ans_right+1] if ans_left >= 0 else ""