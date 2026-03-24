class Solution:
    def maxProfit(self, prices: List[int]) -> int:          
        min_price = prices[0]
        ans = 0
        for p in prices:
            ans = max(ans, p-min_price)
            min_price = min(p,min_price)
        return ans

