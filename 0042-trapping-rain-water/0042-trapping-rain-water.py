class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left,right = 0, len(height)-1
        l_max,r_max = height[0],height[-1]
        while left < right:
            if l_max < r_max:
                left += 1
                l_max = max(l_max, height[left])
                ans += l_max - height[left]
            else:
                right -= 1
                r_max = max(r_max, height[right])
                ans += r_max - height[right]
        return ans