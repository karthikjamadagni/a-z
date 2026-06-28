class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        n = len(prices)
        bp = prices[0]
        for i in range(1, n):
            profit = prices[i] - bp

            maxProfit = max(profit, maxProfit)

            if prices[i] < bp:
                bp = prices[i]

        return maxProfit