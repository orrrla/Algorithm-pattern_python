class Solution:
    def maxProfit(self, prices: List[int]) -> int:          
        def helper(left, right):
            # 递归终止条件
            if left >= right:
                return 0
            # 分割数组
            mid = (left + right) // 2
            # 左右子数组的最大利润
            left_profit = helper(left, mid)
            right_profit = helper(mid + 1, right)

            # 跨边界的最大利润
            left_min = min(prices[left:mid + 1])
            right_max = max(prices[mid + 1:right + 1])
            cross_profit = right_max - left_min
            return max(left_profit, right_profit, cross_profit)
        if not prices or len(prices) < 2:
            return 0

        return helper(0, len(prices) - 1)

